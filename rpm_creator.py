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
        self.__serviceDirPath= serviceDirPath.rstrip("/")
        self.__baseDir       = ""
        self.__specFile      = ""
        self.__srcDir        = ""
        self.__buildRoot     = ""
        self.__specFileName  = ""
        self.__configFileList= []
        self.__buildRootServicePath = ""
        self.__buildRootConfPath = ""
        self.__fileList = []
        self.__dirList	= []

	self.__buildRoot = self.getRPMRoot() + "/BUILDROOT"
        self.validateBaseDirectory(BASE_DIR)
        self.setSrcDir()
        self.setConfDir(CONF_DIR)
        self.setSpecFileName()
        
    def validateBaseDirectory(self,baseDir):
        baseDir = baseDir.rstrip("/")
        if not os.path.exists(baseDir):
            print "Base Directory " + baseDir + " does not exist. Creating the base directory" 
            os.system("mkdir -p "+ baseDir)
        self.setBaseDir(baseDir)

    def setBaseDir(self,baseDir):
        self.__baseDir = baseDir

    def getBaseDir(self):
        return self.__baseDir

    def setSrcDir(self):
        self.__srcDir = self.getBaseDir() +"/"+ self.getService() 

    def setConfDir(self,confDir):
        confDir = confDir.rstrip("/")+ "/" +  self.getService()
        if not  os.path.exists(confDir):
            print "Conf Directory " + confDir + " does not exist. Creating the Conf directory" 
            os.system("mkdir -p "+ confDir)
        self.__confDir = confDir

    def getConfDir(self):
        return self.__confDir

    def setSpecFileName(self):
        self.__specFileName = "angel-"+ self.getService() + "-" + self.getRPMType()\
        + "-" + self.getMajorRev()

    def setBuildRoot(self):
        self.__buildRoot = self.getRPMRoot() + "/BUILDROOT"

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
        return self.__rpmRoot + "/" + self.getService()

    def getBuildRoot(self):
        return self.__buildRoot

	def getLogPath(self):
		return "/var/log/angel/" + service

    def createRPMStructure(self):
        print  "Create RPM Structure.........................................."
	print   "Cleaning out existing directories"
	rpmRoot = self.getRPMRoot()
        rmCommand = "rm -rf " + rpmRoot
	os.system(rmCommand)
        rpmDirs = ["BUILD","BUILDROOT","SRPMS","SOURCES","RPMS","SPECS"]
        for dir in rpmDirs:
            command = "mkdir -p " + rpmRoot + "/" + dir 
            os.system(command)
            print "\tCreating a directory %s in %s"%(dir,rpmRoot)
             
        self.setBuildRoot()

    def copyToBuildRoot(self):
        # @@@ Destinnation directory contains all files , these files are part of the package
        # If this directory does not exist,then no need to create spec file, just exit from the code 
        basePath  = self.__buildRoot + self.__baseDir
        self.__buildRootServicePath = basePath + "/" +  self.__service
        self.__buildRootConfPath    = self.__buildRoot + self.getConfDir()

        if not os.path.exists(os.path.dirname(self.__buildRootConfPath)):
            os.system("mkdir -p " + self.__buildRootConfPath)    
        if not os.path.exists(os.path.dirname(basePath)):
            os.system("mkdir -p  " + self.__buildRootServicePath)
        else:
            if not os.path.exists(os.path.dirname(self.__buildRootServicePath)):
                os.system("mkdir -p  " + self.__buildRootServicePath)

		#makes log directory
		os.system("mkdir -p " +  self.__buildRoot + self.getLogPath())

        print "Copy sources from "+self.__serviceDirPath +" to "+self.__buildRootServicePath 
        os.system("cp -rf   " + self.__serviceDirPath + "/*  " + self.__buildRootServicePath) 
        self.getConfigFileList(self.__buildRootServicePath)
        os.system("cp -rf " + self.__buildRootServicePath  + "/conf/*  "   + self.__buildRootConfPath)
        os.system("rm -rf " + self.__buildRootServicePath+"/conf")

        # We don't want to include '.svn' while creating RPM.
        command = "find " + self.__buildRootServicePath + " -name \*.svn -exec rm -rf {} \;"
        print "Remove .svn from the directory:  "+self.__buildRootServicePath
        print command
        os.system(command) 

    def writeSpecFile(self):
        print "Writing Spec File.............................................."+"\n"
        self.getListOfFilesInService(self.__buildRootServicePath)
        self.__createSpecInfoObj = CreateSpecInformation(self.__service,self.__majorRev,\
        self.__minorRev,self.__rpmType,self.__baseDir,self.__buildRoot,\
        self.getRPMRoot(),self.__srcDir,self.__confDir, self.__configFileList , self.__fileList, self.__dirList)

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
        fp.write(self.__createSpecInfoObj.getPostUnScript())
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
        command = commandName + " " + option + " " + target + " " + "--buildroot " \
        + self.__buildRoot + " " + specFilePath
        print command
        os.system(command)

    def getConfigFileList(self,buildRootServicePath):
        confDirPath = buildRootServicePath+"/conf/"
        print "Conf Dir Path:"+confDirPath
        confDirContent = os.listdir(confDirPath)
        for file in confDirContent:
            absFilePath = confDirPath + file
            if os.path.isfile(absFilePath):
                self.__configFileList.append(file)

    def getListOfFilesInService(self,buildRootServicePath):
        for (path,dir,files)in os.walk(buildRootServicePath):
             self.__dirList.append(path)
             for file in files:
                 absFilePath = path  + "/" + file
                 if not self.checkConfigFile(file): 
                    self.__fileList.append(absFilePath)

    def checkConfigFile(self,file):
    #@@ for check if file is config file.
        for configFile in self.__configFileList:
            if file == configFile:
                return True
            else:
                return False

