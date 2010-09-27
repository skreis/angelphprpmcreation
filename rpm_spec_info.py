#!/usr/bin/python

from rpm_header import *

#@@@ Generate Spec file for creating package.

class CreateSpecInformation:
    def __init__(self , service , majorRevision , minorRevision , rpmType , \
                  baseDir ,destDir , buildDir , buildRoot):
        self.__baseDir          = baseDir
        self.__buildDir         = buildDir
        self.__destDir          = destDir
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
        self.__includeDir       = destDir   
        self.__postScript       = ""
        self.__preScript        = ""
        self.__installSection   = ""
        self.__prepSection      = ""
        self.__buildSection     = ""
        self.__verifyScript     = ""
        self.__cleanScript      = ""
        self.__fileSection      = ""
        self.__defAttribute     = DEFATTR
        self.__docsDirective    = DOCS
        self.__service          = service
        self.__majorRev         = majorRevision
        self.__rpmType          = rpmType

        self.setPreambleSection()
        self.setDescription()
        self.setPrepSection()
        self.setBuildSection()
        self.setInstallSection()
        self.setPostScript()
        self.setPreScript()
        self.setVerifyScript()
        self.setCleanScript()
        self.setFileSection()

       
    def getPackageName(self):
        return "angel-" + self.__service + "-" + self.__rpmType + "-" + self.__majorRev

    def getSummary(self):
        return "angel-" + self.__service + "-" + self.__rpmType

    def setPreambleSection(self):
        self.__preambleSection = "%define base_dir  " + self.__baseDir + "\n"  \
        + "%define config_dest_dir  " + self.__destDir + "\n" \
        + "%define _rpmdir  " + self.__buildDir + "/RPMS" + "\n" \
        + "%define BuildRoot  " + self.__buildRoot + "\n" \
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
        post_install_script = """ if ["$1" = "1"]; then """ + "\n" + "   " \
        + "/usr/sbin/alternatives --install " + self.__baseDir + "/services/" \
        + self.__service + "/" + self.__rpmType + " " + "angel-" + self.__service \
        + "-" + self.__rpmType + "  " + "%" + "(" + self.__destDir + ")" + "\n" \
        + "  " + " echo /usr/sbin/alternatives --install  " + self.__baseDir + \
        "/services/" + self.__service + "/" + self.__rpmType + "  " + "angel-" \
        + self.__service + "-" + self.__rpmType + "  " + self.__destDir + "\n" \
        + " " + "fi"
        if post_install_script != "":
            self.__postScript = "%post" + "\n" + post_install_script + "\n" + "\n"

    def getPostScript(self):
        return self.__postScript
        

    def setPreScript(self):
        pre_uninstall_script = """ if ["$1" = "0"]; then """ + "\n" + "   " \
        +  "/usr/sbin/alternatives --remove " + "angel-" + self.__service + "-" \
        + self.__rpmType + "  " + "%" + "(" + self.__destDir + ")" + "\n" + "  " \
        + "echo /usr/sbin/alternatives --remove angel-" + self.__service + "-" \
        + self.__rpmType + "  "+self.__destDir + "\n" + " " + "fi"

        if pre_uninstall_script != "":
            self.__preScript = "%preun" + "\n" + pre_uninstall_script + "\n" + "\n"

    def getPreScript(self):
        return self.__preScript
            
    def setInstallSection(self):
        if install_cmd != "":
            self.__installSection = "%install" + "\n" + install_cmd + "\n" + "\n" 

    def getInstallSection(self):
        return self.__installSection

    def setPrepSection(self):
        if prep_actions != "":
            self.__prepSection = "%prep" + "\n" + prep_actions + "\n" + "\n"

    def getPrepSection(self):
        return self.__prepSection

    def setBuildSection(self):
        if build_cmd != "":
            self.__buildSection = "%build" + "\n" + build_cmd + "\n" + "\n"

    def getBuildSection(self):
        return self.__buildSection

    def setVerifyScript(self):
        if verify_script != "":
            self.__verifyScript = "%verify" + "\n" + verify_script + "\n" + "\n"

    def getVerifyScript(self):
        return self.__verifyScript

    def setCleanScript(self):
        if clean_script != "":
            self.__cleanScript = "%clean" + "\n" + clean_script + "\n" + "\n"

    def getCleanScript(self):
        return self.__cleanScript

    def setFileSection(self):
        self.__fileSection  = "%files" + "\n" + "%dir" + "  " + self.__includeDir + "\n" 

    def getFileSection(self):
        return self.__fileSection

