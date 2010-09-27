#!/usr/bin/python

# @@@ Update Yum repsitory  
# To update yum repository file /etc/yum.repos.d should be configured.

import os

class UpdateYumRepository:
    def __init__(self,rpmSourceDir,yumRepoDir):
        self.__rpmSourceDir = rpmSourceDir
        self.__yumRepoDir   = yumRepoDir
        self.createRepository()


    def copyRPMs(self):
        copyCommand = "cp " + self.__rpmSourceDir + "/*.rpm " + "  " + self.__yumRepoDir
        os.system(copyCommand)
        

    def createRepository(self):
        if os.path.exists(self.__yumRepoDir):
            self.copyRPMs()
            self.cleanYumRepository()
            print "Executing CreateRepo command....................................."
            os.system("createrepo   " +self.__yumRepoDir)
            self.yumList()
        else:
            print("Yum Local Reository does not exist")    

    def cleanYumRepository(self):
        print "Executing Yum clean command.........................................."
        #  Run this command to   ensure that, nothing unnecessary space used.
        os.system("yum clean all")

    def yumList(self):
        print "Executing Yum list comannd........................................"
        os.system("yum list | grep angel")
        
       
                 



        
