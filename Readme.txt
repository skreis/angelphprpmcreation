			README

Steps to run the script to create an RPM:


Below are the constants values to be set in rpm_header.py to create a spec file 
======================================================

1.  BASE_DIR             : Define base directory(/usr/local/angel.com/psphp).
2.  BUILD_DIR            : Define build directory. 

3.  LICENSE              : 
4.  DISTRIBUTION         : 
5.  GROUP                : 
6.  PREFIX               : 
7.  AUTOPROV             : 
8.  DESCRIPTION          : 
9.  AUTOREQ              : 
10. DEFATTR              : Define default attribute in file section.       
11. ATTR                 : Define attribute in file section.     
12. DOCS                 : Define document file in file section.    

13. PRE_UNINSTALL_SCRIPT : A script string which will be placed in preun directive. 
14. POST_INSTALL_SCRIPT  : A script string which will be placed in post directive. 
15. BUILD_CMD            : Define a build command which will be placed in build directive. 
16. INSTALL_CMD          : Define install command which will be placed in install directive.
17. PREP_ACTIONS         : Define prep actions which will be placed in prep directive.   
18. VERIFY_SCRIPT        : A script string which will be placed in verify directive.
19. CLEAN_SCRIPT         : A script string which will be placed in clean directive.

Configuration :
================
1- Edit /etc/yum.repos.d/rpm.repo with following lines.
[ANGEL]
name = ANGEL
baseurl=file:///tmp/repo
gpgcheck=0
enable=1

Note: /tmp/repo is local repository ,that is created by createrepo command.

Execution:
============
chmod +x rpm_main.py
./rpm_main.py -s <service_name> -r <rpm_type> -i <input_directory> -l <local_repository> -V <major> -v <minor>

i.e.
./rpm_main.py -s starwood -r server -i /tmp/starwood -l /tmp/repo -V 2 -v 3


Error Messages : 
============
1- If your local yum repository directory does not exist.
	Yum Local Reository does not exist message display in output.
2- If Destinaion Directory does not exist.
	Destination Directory  <xxxx>: does not exist.

To execute the script from any where
===============
set PATH env to execute the script from anywhere

If the script file is in /tmp/Josh, then 

$ export PATH=$PATH:/tmp/Josh

$ ./rpm_main.py  -s starwood -V 10 -v 2 -r server -l /home/repo  -I /tmp/workspaces/starwood    -> this command can be executed from anywhere


