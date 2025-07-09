import os


# ************************* Get current UTC datetime in string  *************************#
def getUTCDateTimeString():
    from datetime import datetime

    UTCDateTime = datetime.utcnow()
    return UTCDateTime.strftime("%d%m%Y_%H%M%S")


utcDateTimeString = getUTCDateTimeString()


# ************************* Check if the directory exists *************************#
def checkIfDirExists(dirPath):
    return os.path.exists(dirPath)


# ************************* Create the directory structure for test reports and files *************************#


def initTestDirStructure():
    global testDirPath
    testDirPath = "RVS_Automation_Test_Results"

    if checkIfDirExists(testDirPath):
        pass
    else:
        os.mkdir(testDirPath)

    global testCaseReportsDir
    testCaseReportsDir = testDirPath + "/TestReports"
    if checkIfDirExists(testCaseReportsDir):
        pass
    else:
        os.mkdir(testCaseReportsDir)

    global testCaseImages
    testCaseImages = testDirPath + "/TestImages"
    if checkIfDirExists(testCaseImages):
        pass
    else:
        os.mkdir(testCaseImages)


# ***** Main script execution starts here
initTestDirStructure()

testReportFileName = "RVSAutomationTestResults_" + utcDateTimeString + ".html"
CAPSTestCmd = (
    "python -m pytest --html-report=" + testCaseReportsDir + "/" + testReportFileName
)

os.system(CAPSTestCmd)
