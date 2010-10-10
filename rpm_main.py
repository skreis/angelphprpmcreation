#!/usr/bin/python
import os
import sys
from rpm_header import *
from rpm_creator import *
from rpm_yum_update import *

# Taking command line argument to create RPM and update RPM to yum utility.
if __name__ == '__main__':
    
    from optparse import OptionParser

    parser = OptionParser()

    parser.add_option  ("-s","--service-name",
                          action="store",
                          type="string", 
                          dest="service_name",
                          default="",
                          help="Service Name")
    
    parser.add_option ("-V","--major-version",
                         action="store",
                         type="string",
                         dest="major_version_number",
                         default="",
                         help="Major Version Number")
                       
    parser.add_option ("-v","--minor-version",
                         action="store",
                         type="string",
                         dest="minor_version_number",
                         default="",
                         help="Minor Version Number")
                               
    parser.add_option  ("-r", "--rpm-type",
                          action = "store",
                          type="string",
                          dest="rpm_type",
                          default="",
                          help="RPM Type")
    
    parser.add_option ("-l","--local-repo",
                        action="store",
                        type="string",
                        dest="local_repo",
                        default="",
                        help="Local Repository")

    parser.add_option ("-i","--input-path",
                        action = "store",
                        type="string",
                        dest="input_path",
                        default="",
                        help="Input Path")
                        
    options , remainder = parser.parse_args()

    if(options.service_name!="" and options.major_version_number !="" and options.input_path !=""  \
        and options.minor_version_number and options.rpm_type ):

        if os.path.exists(options.input_path): 
            rpm = CreateRPMPackage(options.service_name , options.major_version_number , options.minor_version_number,\
                                   options.rpm_type , options.input_path )
            rpm.createRPM()
            rpmRoot = rpm.getRPMRoot()
            rpmRoot = rpmRoot.rstrip("/")
            RPMPath = rpmRoot + "/RPMS/noarch"

            if options.local_repo != "":
                UpdateYumRepository(RPMPath,options.local_repo)
        else:
            print "Service Directory  " + options.service_name  + " doesn't exist "
            sys.exit(0)

    else:

        os.system("python rpm_main.py --help") 
