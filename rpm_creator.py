#!/usr/bin/python


# This class does the following
# 1-Create package structure.
# 2-Copy all required files to BuildRoot area.
# 3-Write Spec file.
# 4-Create RPM.

import os
import sys
from rpm_header import *
from rpm_spec_info import *

RPMBUILD = "rpmbuild"
TARGET   = "--target=noarch"
OPTION   = "-bb"
BASE_DIR = "/usr/local/angel.com"


class CreateRPMPackage:

    def __init__(self , service , majorRev , minorRev , rpmType , buildDir):
        self.__service       = service
        self.__majorRev      = majorRev
        self.__minorRev      = minorRev
        self.__rpmType       = rpmType
        self.__rpmRoot       = buildDir
        self.__baseDir       = BASE_DIR
        self.__specFile      = ""
        self.__linkDirName   = ""
        self.__destDir       = ""
        self.__buildRoot     = ""
        self.__specFileName  = ""

        self.setDestDir()
        self.setSpecFileName()
        

    def getDestDir(self):
        return self.__destDirName

    def setBaseDir(self,baseDir):
        self.__baseDir = baseDir

    def getBaseDir(self):
        return self.__baseDir

    def setDestDir(self):
        self.__destDir = self.getBaseDir() + "/builds/" + self.getService() + "-" \
        + self.getRPMType() + "/" + self.getMajorRev()

    def setSpecFileName(self):
        self.__specFileName = "angel-"+ self.getService() + "-" + self.getRPMType()\
        + "-" + self.getMajorRev()

    def setBuildRoot(self):
        self.__buildRoot = self.__rpmRoot + "/BUILDROOT"

    def getLinkDir(self):
        return self.__linkDirName

    def setLinkDir(self):
        self.__linkDir = self.getBaseDir() + "/services" + "-" + self.getService()

    def getService(self):
        return self.__service

    def getMajorRev(self):
        return self.__majorRev

    def getMinorRev(self):
        return self.__minorRev 

    def getRPMType(self):
        return self.__rpmType

    def getSpecFileName(self):
        return self.__specFileName

    def getRPMRoot(self):
        return self.__rpmRoot

    def getBuildRoot(self):
        return self.__buildRoot

    def createRPMStructure(self):
        print  "Create RPM Structure.........................................."+"\n"
        rpmDirs = ["BUILD","BUILDROOT","SRPMS","SOURCES","RPMS","SPECS"]
        rpmRoot = self.getRPMRoot()
        for dir in rpmDirs:
            command = "mkdir -p " + rpmRoot + "/" + dir 
            os.system(command)
            print "Creating Directory %s in %s :"%(dir,rpmRoot)
             
        self.setBuildRoot()

    def copyToBuildRoot(self):
        print "Copy To Build Root (Staging Area).............................." +"\n"
        print "BuildRoot:"+self.__buildRoot
        print "DestDir:"+self.__destDir
        if os.path.exists(self.__destDir):
            buildsPath  = self.__buildRoot + BASE_DIR + "/builds"
            servicePath = buildsPath + "/" +  self.__service + "-" + self.__rpmType
            versionPath = servicePath + "/" + self.__majorRev

            if not os.path.exists(os.path.dirname(buildsPath)):
                os.system("mkdir -p  " + versionPath)
            else:
                if not os.path.exists(os.path.dirname(servicePath)):
                    os.system("mkdir -p  " + versionPath)
                else:
                    if os.path.exists(os.path.dirname(versionPath)):
                        os.system("mkdir -p " + versionPath)
                    
            os.system("cp -rf  " + self.__destDir + "/*  " + versionPath) 
        else:
             print "Destination Directory  " +self.__destDir + ": does not exist"
             sys.exit(0)


    def writeSpecFile(self):
        print "Writing Spec File.............................................."+"\n"
        self.__createSpecInfoObj = CreateSpecInformation(self.__service,self.__majorRev,\
                    self.__minorRev,self.__rpmType,self.__baseDir,self.__destDir,self.__rpmRoot,self.__buildRoot)

        self.__specFile = self.getRPMRoot() + "/SPECS/" + self.getSpecFileName() + ".spec" 

        if os.path.exists(self.__specFile):
            os.system("rm  " + self.__specFile)

        fp = file(self.__specFile,'a')
        fp.write(self.__createSpecInfoObj.getPreambleSection())
        fp.write(self.__createSpecInfoObj.getDescription())
        fp.write(self.__createSpecInfoObj.getPrepSection()) 
        fp.write(self.__createSpecInfoObj.getBuildSection())
        fp.write(self.__createSpecInfoObj.getInstallSection()) 
        fp.write(self.__createSpecInfoObj.getPostScript())
        fp.write(self.__createSpecInfoObj.getPreScript()) 
        fp.write(self.__createSpecInfoObj.getVerifyScript()) 
        fp.write(self.__createSpecInfoObj.getCleanScript())
        fp.write(self.__createSpecInfoObj.getFileSection())

        fp.close()


    def createRPM(self):
        self.createRPMStructure()
        self.copyToBuildRoot()
        self.writeSpecFile()
        self.runRPMBuildCommand(RPMBUILD , OPTION , TARGET , self.__specFile)

    def runRPMBuildCommand(self,commandName , option , target , specFilePath):
        print "Executing RPM build command..................................."
        command = commandName + " " + option + " " + target + " " + specFilePath
        os.system(command)
        
