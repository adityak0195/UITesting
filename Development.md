### Working Procedures

1. Automation scripts are saved under CAPS, CVS or RVS based on the functionlaity under testing.

    ![image](https://github.com/KB-smartProduction/UITesting/assets/133857066/778d9ad6-09f4-45c8-abd2-79b7ec0c512c)

2. Before starting to write a test script, a JIRA task should be created under [TWX-2813](https://knorr-bremse.atlassian.net/browse/TWX-2813).
   Make sure the the new task created has **_ConsistsOf_** relationships to TWX-2813.

   - **Naming convention for Tasks:** Title of Task is named following \<Functional Area> - \<Major Dashboard Name>, for eg: CAPS - AndOn Department Test script, CVS - DMS Test Script
  
   - **Description** of Task mentions a brief about the test steps and their validation criteria.
  
   - **Attachment:** An excel document is attached with details on test steps.

### Code


**Framework:** unittest is a automation testing framework inspired by jUnit and enables to write test code with object-oriented approach. More documentation [here](https://docs.python.org/3/library/unittest.html).
     

1.  **Python Imports:** Below is a list of import modules needed for folder provisioning and screenshots.

    ```
    from selenium import webdriver
    from selenium.webdriver.edge.options import Options
    from pytest_html_reporter import attach
    from selenium.webdriver.common.by import By
    from time import sleep
    from pyshadow.main import Shadow
    import unittest
    import os
    ```

2.  **setUp():** an instance of driver is initialized and passed as instruction to all tests included in a test case.
   
    ```
    def setUp(self):
        global driver
        self.driver = webdriver.Edge(options=options)
        self.driver.maximize_window()
    ```    

3.  **Edge Browser Options:** Selenium Python uses _Options()_ to specify Microsoft capabilities.

    > _Note: All test scripts simulate test cases in headless mode of browser._

    This is implemented as below:

    ```
    options = Options()
    options.add_argument("--headless")
    ```

    
4.  **Folder Provisioning:** As mentioned in [Intro](https://github.com/KB-smartProduction/UITesting/blob/main/README.md), all screenshots are placed under TestImages folder.

    This is achieved as shown below.

    ```
    def checkIfDirExists(dirPath):
        return os.path.exists(dirPath)
    
    global testDirPath
    testDirPath = "./CVS_Automation_Test_Results/TestImages"
    testpath = testDirPath + "/IChart"
        
    if checkIfDirExists(testpath):
        pass
    else:
        os.mkdir(testpath)
        
    testDirPath1 = "./CVS_Automation_Test_Results/TestImages/IChart/"

    ```
  
