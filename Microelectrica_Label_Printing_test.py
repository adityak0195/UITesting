from selenium import webdriver
from selenium.webdriver.edge.options import Options
from pytest_html_reporter import attach
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from pyshadow.main import Shadow
from PIL import Image
import unittest
import os

options = Options()
options.add_argument("--headless")
testPathImages = "./RVS_Automation_Test_Results/TestImages"
testImage=testPathImages+"/MicroelectricaLabelPrinting"
def checkIfDirExists(dirPath):
    return os.path.exists(dirPath)
 
if checkIfDirExists(testImage):
    pass
else:
    os.mkdir(testImage)
testDirPath = "./RVS_Automation_Test_Results/TestImages/MicroelectricaLabelPrinting/"

class TestClass(unittest.TestCase):
    def __init__(self, driver):
        super().__init__(driver)

    def setUp(self):
        global driver
        self.driver = webdriver.Edge(options=options)
        #self.driver.maximize_window()
        
    def test_demo(self):
        self.driver.get("https://smartproductionrvstest.corp.knorr-bremse.com/Thingworx/Mashups/KBLabelPrintMashup?appKey=a59beff9-da8f-4700-ab43-240c97e0ac1a&x-thingworx-session=true")
        sleep(30)
        try:
            self.driver.execute_script("document.body.style.zoom='60%'")
            #self.driver.set_window_size(1920,1080)
            sleep(10)
            self.driver.save_screenshot(testDirPath +"LabelPrintingPage.png")
            self.searchorder()
            self.reset()
            self.chooseline_dropdown()
            self.setup_checkbox()
            self.dropdowns()
            #self.printlabel()
            
                        
        finally:
            self.driver.quit()
    
    def searchorder(self):
        orderNum=self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_ptcstextfield-44"]')
        orderNum.send_keys("100070447")
        self.driver.save_screenshot(testDirPath +"OrderNum_textfield.png")
        sleep(20)
        self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_ptcsbutton-58"]').click()
        self.driver.save_screenshot(testDirPath +"after_search_button.png")
        shadow=Shadow(self.driver)
        order_dropdown_value=shadow.find_element("ptcs-textfield#root_pagemashupcontainer-5_ptcstextfield-44>div[part='root']>div[part='text-box']>span[id='maskShell']>input[id='input']")
        order_dropdown_value_aria_label=order_dropdown_value.get_attribute('value')
        self.assertEqual(order_dropdown_value_aria_label,"100070447","Order not matched")
        print("Order matched")
        sleep(20)
    def reset(self):
        self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_ptcsbutton-59"]').click()
        self.driver.save_screenshot(testDirPath +"Reset_button.png")
        sleep(3)
        
    def chooseline_dropdown(self):
        self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_ptcsdropdown-11"]').click()
        self.driver.save_screenshot(testDirPath + "chooseLine_dropdown.png")
        sleep(4)
        shadow=Shadow(self.driver)
        '''iframe =shadow.find_element("ptcs-list#root_pagemashupcontainer-5_ptcsdropdown-11-external-wc>div[part='list-container']>ptcs-v-scroller#chunker>div>div>ptcs-list-item[index='1']")
        scroll_origin = ScrollOrigin.from_element(iframe)
        ActionChains(self.driver).scroll_from_origin(scroll_origin, 0, 1000).perform()
        self.driver.save_screenshot("chooseLine_dropdown.png")'''
        shadow=Shadow(self.driver)
        root1=shadow.find_element("ptcs-list#root_pagemashupcontainer-5_ptcsdropdown-11-external-wc>div[part='list-container']>ptcs-v-scroller#chunker>div>div>ptcs-list-item[index='1']").click()
        self.driver.save_screenshot(testDirPath + "selectedLine.png")
        sleep(4)
        chooseline_dropdown_value=shadow.find_element("ptcs-dropdown#root_pagemashupcontainer-5_ptcsdropdown-11>ptcs-hbar#select>ptcs-list-item[part='list-item']")
        chooseline_dropdown_value_aria_label=chooseline_dropdown_value.get_attribute('aria-label')
        self.assertEqual(chooseline_dropdown_value_aria_label,"KBRVSMILSwsL4TestBenchStationThing","chooseline not matched")
        print("chooseline matched")
    def setup_checkbox(self):
        self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_ptcscheckbox-32"]').click()
        self.driver.save_screenshot(testDirPath + "SerialNum_checkbox.png")
        sleep(10)   
        self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_ptcscheckbox-32"]').click()
        self.driver.save_screenshot(testDirPath + "SerialNum_checkbox.png")
        sleep(10) 
        self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_ptcscheckbox-38"]').click()
        self.driver.save_screenshot(testDirPath +"chooseLine_dropdown.png")
        sleep(14)
    def dropdowns(self):
        self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_ptcsdropdown-12"]').click()
        sleep(15)
        self.driver.save_screenshot(testDirPath +"orderdropdown.png")
        shadow=Shadow(self.driver)
        root1=shadow.find_element("ptcs-list#root_pagemashupcontainer-5_ptcsdropdown-12-external-wc>div[part='list-container']>ptcs-v-scroller#chunker>div>div>ptcs-list-item[index='1']").click()
        self.driver.save_screenshot(testDirPath +"orderselected.png")
        sleep(4)
        order_dropdown_value=shadow.find_element("ptcs-dropdown#root_pagemashupcontainer-5_ptcsdropdown-12>ptcs-hbar#select>ptcs-list-item[part='list-item']")
        order_dropdown_value_aria_label=order_dropdown_value.get_attribute('aria-label')
        self.assertEqual(order_dropdown_value_aria_label,"100071406","order not matched")
        print("order matched")
        self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_ptcsdropdown-27"]').click()
        sleep(5)
        self.driver.save_screenshot(testDirPath +"serialnumdropdown.png")
        shadow=Shadow(self.driver)
        root1=shadow.find_element("ptcs-list#root_pagemashupcontainer-5_ptcsdropdown-27-external-wc>div[part='list-container']>ptcs-v-scroller#chunker>div>div>ptcs-list-item[index='0']").click()
        self.driver.save_screenshot(testDirPath +"serialnum.png")
        sleep(4)
        order_dropdown_value=shadow.find_element("ptcs-dropdown#root_pagemashupcontainer-5_ptcsdropdown-27>ptcs-hbar#select>ptcs-list-item[part='list-item']")
        order_dropdown_value_aria_label=order_dropdown_value.get_attribute('aria-label')
        self.assertEqual(order_dropdown_value_aria_label,"7625030340","order not matched")
        print("serial matched")
    def printlabel(self):
        self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_ptcsbutton-13"]').click()
        sleep(5)
        

    def screenshot_on_failure(self):
        attach(data=self.driver.get_screenshot_as_png())
        
if __name__ == "__main__":
    unittest.main()
