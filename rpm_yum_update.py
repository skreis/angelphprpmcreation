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
            print "Executing CreateRepo command....................................."
            os.system("createrepo   " +self.__yumRepoDir)
        else:
            print("Yum Local Reository does not exist")    

       
                 



        
