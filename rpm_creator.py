#!/usr/bin/python

# This class does the following
# 1-Create package structure.
# 2-Copy all required files to BuildRoot staging area.
# 3-Write the Spec file.
# 4-Create RPM.

import os
import sys
from rpm_header import *
from rpm_spec_info import *

RPMBUILD = "rpmbuild"
TARGET   = "--target=noarch"
OPTION   = "-bb"


class CreateRPMPackage:

    def __init__(self , service , majorRev , minorRev , rpmType , serviceDirPath ):
        self.__service       = service
        self.__majorRev      = majorRev
        self.__minorRev      = minorRev
        self.__rpmType       = rpmType
        self.__rpmRoot       = BUILD_DIR
        self.__serviceDirPath= serviceDirPath
        self.__baseDir       = ""
        self.__specFile      = ""
        self.__srcDir        = ""
        self.__buildRoot     = ""
        self.__specFileName  = ""
        self.__configFileList= []

        self.validateBaseDirectory(BASE_DIR)
        self.setSrcDir()
        self.setSpecFileName()
        
    def validateBaseDirectory(self,baseDir):
        baseDir = baseDir.rstrip("/")
        if os.path.exists(baseDir):
            print "Base Directory " + baseDir + " exists" 
            self.setBaseDir(baseDir)
        else:
            print "Base Directory " + baseDir + " does not exist. Please provide the valid base directory path" 
            sys.exit(0)

    def setBaseDir(self,baseDir):
        self.__baseDir = baseDir

    def getBaseDir(self):
        return self.__baseDir

    def setSrcDir(self):
        self.__srcDir = self.getBaseDir() +"/"+ self.getService() 
        if not os.path.exists(self.__srcDir):
            os.system("mkdir -p " + self.__srcDir)

    def setSpecFileName(self):
        self.__specFileName = "angel-"+ self.getService() + "-" + self.getRPMType()\
        + "-" + self.getMajorRev()

    def setBuildRoot(self):
        self.__buildRoot = self.__rpmRoot + "/BUILDROOT"

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

        print  "Create RPM Structure.........................................."
        rpmDirs = ["BUILD","BUILDROOT","SRPMS","SOURCES","RPMS","SPECS"]
        rpmRoot = self.getRPMRoot()
        for dir in rpmDirs:
            command = "mkdir -p " + rpmRoot + "/" + dir 
            os.system(command)
            print "\tCreating a directory %s in %s"%(dir,rpmRoot)
             
        self.setBuildRoot()

    def copyToBuildRoot(self):

        # @@@ Destinnation directory contains all files , these files are part of the package
        # If this directory does not exist,then no need to create spec file, just exit from the code 
        if os.path.exists(self.__srcDir):
            basePath  = self.__buildRoot + self.__baseDir
            servicePath = basePath + "/" +  self.__service  
            if not os.path.exists(os.path.dirname(basePath)):
                os.system("mkdir -p  " + servicePath)
            else:
                if not os.path.exists(os.path.dirname(servicePath)):
                    os.system("mkdir -p  " + servicePath)

            print "Copy sources from "+self.__serviceDirPath +" to "+self.__srcDir 
            os.system("cp -rf   " + self.__serviceDirPath + "/*  " + self.__srcDir) 
            os.system("cp -rf " + self.__srcDir  + "/conf/*  "   + self.__srcDir)
            os.system("rm -rf " + self.__srcDir+"/conf")

            # We don't want to include '.svn' while creating RPM.
            command = "find " + self.__srcDir + " -name \*.svn -exec rm -rf {} \;"
            print "Remove .svn from the directory:  "+self.__srcDir
            print command
            os.system(command) 

            print "Copy sources from "+self.__srcDir +" to "+servicePath
            os.system("cp -rf  " + self.__srcDir + "/*  " + servicePath)
        else:
            print "Source Directory  " +self.__srcDir + ": does not exist"
            sys.exit(0)

    def writeSpecFile(self):

        print "Writing Spec File.............................................."+"\n"
        self.setConfigFileList()
        self.__createSpecInfoObj = CreateSpecInformation(self.__service,self.__majorRev,\
        self.__minorRev,self.__rpmType,self.__baseDir,self.__srcDir,self.__rpmRoot,self.__buildRoot,\
        self.__configFileList)

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
        print "Execute RPM build command..................................."
        command = commandName + " " + option + " " + target + " " + specFilePath
        os.system(command)

    def setConfigFileList(self):
        confDirPath = self.__serviceDirPath+"/conf/"
        confDirContent = os.listdir(confDirPath)
        for file in confDirContent:
            absFilePath = confDirPath + file
            if os.path.isfile(absFilePath):
                self.__configFileList.append(file)
        
