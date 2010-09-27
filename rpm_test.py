from rpm_creator import *
from rpm_yum_update import *
rpm = CreateRPMPackage("script","1.0","1.0","server","/usr/local/angel.com","/home/sudheer")
rpm.createRPM()
yum = UpdateYumRepository("/home/sudheer/RPMS/noarch","/home/repo")



