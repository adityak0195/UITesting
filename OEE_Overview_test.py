from selenium import webdriver
from selenium.webdriver.edge.options import Options
from pytest_html_reporter import attach
from time import sleep
from pyshadow.main import Shadow
import unittest
import os

options = Options()
options.add_argument("--headless")

testPathImages = "./RVS_Automation_Test_Results/TestImages"
testImage=testPathImages+"/OEE_Overview"
def checkIfDirExists(dirPath):
    return os.path.exists(dirPath)
 
if checkIfDirExists(testImage):
    pass
else:
    os.mkdir(testImage)

testDirPath = "./RVS_Automation_Test_Results/TestImages/OEE_Overview/"

class TestClass(unittest.TestCase):
    def __init__(self, driver):
        super().__init__(driver)

    def setUp(self):
        global driver
        self.driver = webdriver.Edge(options=options)
        #self.driver.maximize_window()
        
    def test_demo(self):
        self.driver.get("https://smartproductionrvstest.corp.knorr-bremse.com/Thingworx/Mashups/KBProductionAdvisorRailMashup?appKey=a59beff9-da8f-4700-ab43-240c97e0ac1a&x-thingworx-session=true")
        sleep(20)        
        try:
            #self.driver.set_window_size(1920,1080)
            #sleep(30)
            #self.driver.execute_script("document.body.style.zoom='50%'")
            sleep(10)
            self.driver.save_screenshot(testDirPath + "OeeOverviewPage_1.png")
            self.baseTest()
            self.buttonTest()
        finally:
            self.driver.quit()
            
            
    def baseTest(self):
        shadow=Shadow(self.driver)
        root1=shadow.find_element("ptcs-dropdown#root_pagemashupcontainer-5_ptcsdropdown-6>ptcs-hbar#select").click()
        sleep(5)
        self.driver.save_screenshot(testDirPath + "Calculation_base_dropdown_2.png")
        sleep(10)
        shadow=Shadow(self.driver)
        root1=shadow.find_element("ptcs-list#root_pagemashupcontainer-5_ptcsdropdown-6-external-wc>div[part='list-container']>ptcs-v-scroller#chunker>div>div>ptcs-list-item[index='0']").click()
        sleep(15)
        self.driver.save_screenshot(testDirPath + "Calculation_base_selected_3.png")
        
        
        shadow.find_element("ptcs-button#cell_KBProductionAdvisorRailSingleMachineMashup-1_ptcsbutton-39.ptcs-wrapper.widget-content.widget-ptcsbutton").click()
        sleep(10)
        self.driver.save_screenshot(testDirPath + "Line_selected_E13.png")
        self.driver.find_element("xpath",'//*[@id="cell_KBProductionAdvisorRailSingleMachineMashup-1_navigationfunction-63-popup"]/div[1]/span[2]').click()
        sleep(10)
        self.driver.save_screenshot(testDirPath + "Lineclose_E13.png")
        
        
    def buttonTest(self):
        self.driver.find_element("xpath",'//*[@id="cell_KBProductionAdvisorRailSingleMachineMashup-1_ptcsbutton-51"]').click()
        sleep(20)
        self.driver.save_screenshot(testDirPath + "KPIopen.png")
        self.driver.find_element("xpath",'//*[@id="cell_KBProductionAdvisorRailSingleMachineMashup-1_navigationfunction-64-popup"]/div[1]/span[2]').click()
        sleep(2)
        self.driver.save_screenshot(testDirPath + "KPIclosed.png")
        
        self.driver.find_element("xpath",'//*[@id="cell_KBProductionAdvisorRailSingleMachineMashup-1_ptcsbutton-52"]').click()
        sleep(10)
        self.driver.save_screenshot(testDirPath + "Partsopened.png")
        self.driver.find_element("xpath",'//*[@id="cell_KBProductionAdvisorRailSingleMachineMashup-1_navigationfunction-65-popup"]/div[1]/span[2]').click()
        sleep(2)
        self.driver.save_screenshot(testDirPath + "Partsclosed.png")
        self.driver.find_element("xpath",'//*[@id="cell_KBProductionAdvisorRailSingleMachineMashup-1_ptcsbutton-53"]').click()
        sleep(10)
        self.driver.save_screenshot(testDirPath + "Statusopened_10.png")
        self.driver.find_element("xpath",'//*[@id="cell_KBProductionAdvisorRailSingleMachineMashup-1_navigationfunction-66-popup"]/div[1]/span[2]').click()
        sleep(2)
        self.driver.save_screenshot(testDirPath + "Statusclosed_11.png")
        self.driver.find_element("xpath",'//*[@id="cell_KBProductionAdvisorRailSingleMachineMashup-1_ptcsbutton-54"]').click()
        sleep(10)
        self.driver.save_screenshot(testDirPath + "MessageOpened_12.png")
        self.driver.find_element("xpath",'//*[@id="cell_KBProductionAdvisorRailSingleMachineMashup-1_navigationfunction-67-popup"]/div[1]/span[2]').click()
        sleep(2)
        self.driver.save_screenshot(testDirPath + "MessageClosed_13.png")
    def screenshot_on_failure(self):
        attach(data=self.driver.get_screenshot_as_png())
if __name__ == "__main__":
    unittest.main()  
