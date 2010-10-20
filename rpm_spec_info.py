#!/usr/bin/python

from rpm_header import *

#@@@ Generate Spec file for creating package.

class CreateSpecInformation:
    def __init__(self , service , majorRevision , minorRevision , rpmType , \
                  baseDir , buildRoot , buildDir , sourceDir , confDir , \
				 configFileList , fileList, dirList, rpmCreator):
        self.__baseDir          = baseDir
        self.__buildDir         = buildDir
        self.__sourceDir        = sourceDir
        self.__confDir          = confDir
        self.__buildRoot        = buildRoot
        self.__version          = minorRevision
        self.__release          = minorRevision
        self.__summary          = ""
        self.__license          = LICENSE
        self.__distribution     = DISTRIBUTION
        self.__group            = GROUP
        self.__autoprov         = AUTOPROV 
        self.__autoreq          = AUTOREQ
        self.__prefix           = PREFIX
        self.__description      = DESCRIPTION
        self.__preambleSection  = ""
        self.__postScript       = ""
        self.__preScript        = ""
        self.__installSection   = ""
        self.__prepSection      = ""
        self.__buildSection     = ""
        self.__verifyScript     = ""
        self.__cleanScript      = ""
        self.__postUnScript     = ""
        self.__fileSection      = ""
        self.__defAttribute     = DEFATTR
        self.__docsDirective    = DOCS
        self.__service          = service
        self.__majorRev         = majorRevision
        self.__rpmType          = rpmType
        self.__configFileList   = configFileList
        self.__fileList         = fileList
        self.__dirList			= dirList
		self.__rpmCreator		= rpmCreator
        self.setPreambleSection()
        self.setDescription()
        self.setPrepSection()
        self.setBuildSection()
        self.setInstallSection()
        self.setPostScript()
        self.setPostUnScript()
        self.setPreScript()
        self.setVerifyScript()
        self.setCleanScript()
        self.setFileSection()

       
    def getPackageName(self):
        return "angel-" + self.__service + "-" + self.__rpmType + "-" + self.__majorRev

    def getSummary(self):
        return "angel-" + self.__service + "-" + self.__rpmType

	def getRpmCreator(self):
		return __rpmCreator

    def setPreambleSection(self):
        self.__preambleSection = "%define base_dir  " + self.__baseDir + "\n"  \
        + "%define config_dest_directory  " + self.__sourceDir + "\n" \
        + "%define _rpmdir  " + self.__buildDir + "/RPMS" + "\n" \
        + "Name:" + self.getPackageName() + "\n" \
        + "Version:" + self.__version + "\n" \
        + "Release:" + self.__release + "\n" \
        + "Summary:" + self.getSummary() + "\n" \
        + "License:" + self.__license + "\n" \
        + "Distribution:" + self.__distribution + "\n" \
        + "Group:" + self.__group + "\n" \
        + "autoprov:" + self.__autoprov + "\n" \
        + "autoreq:" + self.__autoreq + "\n" \
        + "Prefix:" + self.__prefix + "\n" + "\n"

    def setDescription(self):
        self.__description = "%description "+ "\n" + self.__description + "\n" + "\n"

    def getDescription(self):
        return self.__description

    def getPreambleSection(self):
        return self.__preambleSection

    def setPostScript(self):
        if  POST_INSTALL_SCRIPT != "":
            post_install_script = """ if ["$1" = "1"]; then """ + "\n" \
            + "   " + POST_INSTALL_SCRIPT + "\n" + " fi"
            self.__postScript = "%post" + "\n" + post_install_script + "\n" + "\n"

    def getPostScript(self):
        return self.__postScript
        

    def setPreScript(self):
        if  PRE_UNINSTALL_SCRIPT != "":
            pre_uninstall_script = """ if ["$1" = "0"]; then """ + "\n" \
            + "   " + PRE_UNINSTALL_SCRIPT + "\n" + " fi" 

            self.__preScript = "%preun" + "\n" + pre_uninstall_script + "\n" + "\n"

    def setPostUnScript(self):
	self.___postUnScript = ""
#        self.__postUnScript = "%postun" + "\n" + " rm -rf " + self.__baseDir + "/" \
#        + self.__service + "\n" \
#        + " rm -rf " + self.__confDir + "\n\n"

    def getPreScript(self):
        return self.__preScript
            
    def setInstallSection(self):
        if INSTALL_CMD != "":
            self.__installSection = "%install" + "\n" + INSTALL_CMD + "\n" + "\n" 

    def getInstallSection(self):
        return self.__installSection

    def setPrepSection(self):
        if PREP_ACTIONS != "":
            self.__prepSection = "%prep" + "\n" + PREP_ACTIONS  + "\n" + "\n"

    def getPrepSection(self):
        return self.__prepSection

    def setBuildSection(self):
        if BUILD_CMD != "":
            self.__buildSection = "%build" + "\n" + BUILD_CMD + "\n" + "\n"

    def getBuildSection(self):
        return self.__buildSection

    def setVerifyScript(self):
        if VERIFY_SCRIPT != "":
            self.__verifyScript = "%verify" + "\n" + VERIFY_SCRIPT + "\n" + "\n"

    def getVerifyScript(self):
        return self.__verifyScript

    def setCleanScript(self):
        if CLEAN_SCRIPT != "":
            self.__cleanScript = "%clean" + "\n" + CLEAN_SCRIPT + "\n" + "\n"

    def getCleanScript(self):
        return self.__cleanScript

    def setFileSection(self):
	fileSectionPreamble = """
%files
%defattr(644,psuser,psunixusers,755)		
"""
        self.__fileSection = fileSectionPreamble  
        for dir in self.__dirList:
            strlen = len(self.__buildRoot)
			attrs = ""
			relativeDir = dir[strlen:]
			if(relativeDir == self.getRpmCreator().getLogPath())
				attrs = "%attr(755,apache,apache)"
			if(dir != )
            self.__fileSection = self.__fileSection + "%dir " + attrs + relativeDir + "\n"
            
        for file in self.__fileList:
            strlen = len(self.__buildRoot)
            self.__fileSection = self.__fileSection +  file[strlen:]+ "\n"
        for configFile in self.__configFileList:
            self.__fileSection = self.__fileSection + "%config(noreplace) " \
            + self.__confDir + "/" +  configFile + "\n"
        
    def getFileSection(self):
        return self.__fileSection

    def getPostUnScript(self):
        return self.__postUnScript

