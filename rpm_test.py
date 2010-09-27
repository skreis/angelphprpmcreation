from rpm_creator import *
from rpm_yum_update import *
rpm = CreateRPMPackage("script","1.0","1.0","server","/tmp")
rpm.createRPM()
yum = UpdateYumRepository("/tmp/RPMS/noarch","/tmp/repo")

