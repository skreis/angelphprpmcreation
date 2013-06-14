#!/usr/local/bin/python

# The following script utilizes the magic of fpm
# (https://github.com/jordansissel/fpm/wiki) to create a PHP application RPM
# suitable for our production environment.
#
# An advantage to this process as opposed to the other rpm_main.py script is
# that this utilizes a much simpler process using FPM and includes the SVN
# revision info and branch when constructing the package.
#
# usage: ./build_rpm.py -n <package name> -V <major version> -v <minor version> -p <path> -s <scm> -r <repopath>
#
# structure:
#    /usr/local/angel.com/psphp/ = executable scripts
#    /usr/local/angel.com/psphpconf/ = application configuration (inaccessible to world)
#    /var/log/angel/psphp-[package name]/ = default application log location
#

import getopt, sys, os, tempfile, shutil, subprocess, atexit

def main(argv):

    global package_name, major_version, minor_version, path, scm, repo_path, temp_path, post_install

    try:
        opts, args = getopt.getopt(argv, "hn:V:v:p:s:r:", ["help", "name=", "major=", "minor=", "path=", "scm=", "repopath="])

    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)

    for o, a in opts:
        if o in ('-h', '--help'):
            usage()
            sys.exit()
        elif o in ('-n', '--name'):
            print 'package name = %s' % a
            package_name = a
        elif o in ('-V', '--major'):
            print 'major version = %s' % a
            major_version = a
        elif o in ('-v', '--minor'):
            print 'minor version = %s' % a
            minor_version = a
        elif o in ('-p', '--path'):
            print 'path = %s' % a
            path = a
        elif o in ('-s', '--scm'):
            print 'scm = %s' % a
            scm = a
        elif o in ('-r', '--repopath'):
            print 'repopath = %s' % a
            repo_path = a
        else:
            assert False, 'unhandled option'

	# build the description string used in the RPM
    # this is the URL to the branch and the revision number
    rpm_desc = builddesc(scm)
    print 'branch:revision = %s' % rpm_desc

    angel_package_name = 'angel-%s-php' % package_name
    print 'angel package name = %s' % angel_package_name

    # create temp directory
    temp_path = tempfile.mkdtemp()
    temp_data_dir = temp_path + '/data'
    print 'Temporary staging location = %s' % temp_path
    # build the paths to the psphp & psphpconf directories
    psphp_dir = '%s/usr/local/angel.com/psphp/%s' % ( temp_data_dir, package_name )
    psphpconf_dir = '%s/usr/local/angel.com/psphpconf/%s' % ( temp_data_dir, package_name )
    log_dir = '%s/var/log/angel/psphp-%s' % ( temp_data_dir, package_name )

    # create logdir
    os.makedirs(log_dir)

    print 'Copying data from %s => %s, ignoring the conf/ directory and any scm dirs' % ( path, psphp_dir )
    # copy app contents to temporary staging area (excluding conf dir)
    shutil.copytree(path, psphp_dir, ignore=shutil.ignore_patterns('conf', '.svn', '.git'))

    print 'Copying data from %s/conf => %s, ignoring any scm dirs' % ( path, psphpconf_dir )
    # copy config contents to temporary staging area
    shutil.copytree( '%s/conf' % path, psphpconf_dir, ignore=shutil.ignore_patterns('.svn', '.git'))

    print 'Creating post install script'
    post_install = createpostinstall()

    # build fpm command
    fpm_command = "fpm -p '%s' "\
                 "-a all "\
                 "-t rpm "\
                 "-s dir "\
                 "--name '%s' "\
                 "--version '%s' "\
                 "--iteration '%s' "\
                 "--exclude '**/.svn/**' "\
                 "--depends 'angel_ps_php_base' "\
                 "--post-install '%s' "\
                 "--description '%s' "\
                 "-C '%s' ." % (temp_path, angel_package_name, major_version, minor_version, post_install, rpm_desc, temp_data_dir)

    # change to temp dir and run fpm
    os.system('cd %s; %s' % ( temp_path, fpm_command))

    # construct rpm name
    rpm_name = '%s-%s-%s.noarch.rpm' % (angel_package_name, major_version, minor_version)
    print 'RPM name = %s' % rpm_name

    # copy rpm to repo
    print 'Copying RPM to repo %s => %s' % (rpm_name, repo_path)
    shutil.copy('%s/%s' % (temp_path, rpm_name), repo_path)

    # update repo
    print 'Updating repo %s' % repo_path
    os.system('createrepo --update %s' % repo_path)

def builddesc(scm):
    branch = ""
    revision = ""
    if "svn" == scm:
        branch = getoutput("svn info '%s' | awk '/^URL:/ {print $2}'" % path)
        revision = getoutput("svn info '%s' | awk '/^Revision:/ {print $2}'" % path)
    elif "git" == scm:
        branch = getoutput("git --git-dir='%s/.git' name-rev --name-only HEAD")
        revision = getoutput("git --git-dir='%s/.git' rev-parse HEAD")

    # return branch:revision
    return "%s %s %s" % ( scm, branch.strip(), revision.strip() )

def createpostinstall():
    postinstall = """
#!/bin/sh
chown -R apache:apache /var/log/angel/psphp-%s/
chown -R psuser:psunixusers /usr/local/angel.com/psphp/%s/
chown -R psuser:psunixusers /usr/local/angel.com/psphpconf/%s/
chmod 0755 /var/log/angel/psphp-%s/
chmod 0755 /usr/local/angel.com/psphp/%s/
chmod 0755 /usr/local/angel.com/psphpconf/%s/
    """ % (package_name, package_name, package_name, package_name, package_name, package_name)
    tmp_script = tempfile.mkstemp(suffix='.sh')
    os.write(tmp_script[0], postinstall)
    return tmp_script[1]

def getoutput(command):
    proc = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return out

def usage():
    usage = """
    Creates a PHP-specific RPM using FPM for use in packaging the Professional
    Service PHP applications.

    -h --help                 Prints this
    -n --name                 The name of the RPM to create
    -V --major                The package major version
    -v --minor                The package minor version
    -p --path                 The path to the files to include
    -s --scm                  The source control system used [svn|git] - used
                              to provide RPM summary containing branch/version
    -r --repopath             The path to the repo to store to/update
    """
    print usage

@atexit.register
def cleanup():
    print 'Deleting temporary work directory %s' % temp_path
    shutil.rmtree(temp_path)
    print 'Deleting temporary post install script %s' % post_install
    os.remove(post_install)

if __name__ == '__main__':
    main(sys.argv[1:])

