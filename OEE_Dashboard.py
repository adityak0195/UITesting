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
testImage=testPathImages+"/OEE_Dashboard"
def checkIfDirExists(dirPath):
    return os.path.exists(dirPath)
 
if checkIfDirExists(testImage):
    pass
else:
    os.mkdir(testImage)

testDirPath = "./RVS_Automation_Test_Results/TestImages/OEE_Dashboard/"

class TestClass(unittest.TestCase):
    def __init__(self, driver):
        super().__init__(driver)

    def setUp(self):
        global driver
        self.driver = webdriver.Edge(options=options)
        #self.driver.maximize_window()     
    def test_demo(self):
        self.driver.get("https://smartproductionrvstest.corp.knorr-bremse.com/Thingworx/Mashups/KBLocalSmartKPIRailFrameMachineLevelMashup?appKey=a59beff9-da8f-4700-ab43-240c97e0ac1a&x-thingworx-session=true")
        try:             
            sleep(50)
            self.driver.save_screenshot(testDirPath + "OEE_Dashboard_1.png")
            #self.driver.set_window_size(1920,1080)
            sleep(50)
            self.driver.execute_script("document.body.style.zoom='40%'")
            sleep(20)
            self.line()
            self.dropdown()
            self.calendar()
            self.refresh_btn()
            self.checkbox()
                        
        finally:
            self.driver.quit()
    
    def line(self):
        shadow=Shadow(self.driver)
        #root1=shadow.find_element("ptcs-list#root_pagemashupcontainer-5_pt
        root1=shadow.find_element("ptcs-list#root_pagemashupcontainer-5_ptcslist-13>div[part='list-container']>ptcs-v-scroller#chunker>div>div>ptcs-list-item[index='3']").click()
        sleep(3)
        self.driver.save_screenshot(testDirPath + "line_dropdown_2.png")
    
    def dropdown(self):
        self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_mashupcontainer-170_ptcsdropdown-178"]').click()
        sleep(5)
        self.driver.save_screenshot(testDirPath + "CalculationBase_dropdown_3.png")
        shadow=Shadow(self.driver)
        root1=shadow.find_element("ptcs-list#root_pagemashupcontainer-5_mashupcontainer-170_ptcsdropdown-178-external-wc>div[part='list-container']>ptcs-v-scroller#chunker>div>div>ptcs-list-item[index='1']").click()
        sleep(5)
        self.driver.save_screenshot(testDirPath + "Day_selected_4.png")
        
    def calendar(self):
        self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_mashupcontainer-170_timeselector-179"]/div/div[1]/div/div[1]').click()
        sleep(3)
        self.driver.save_screenshot(testDirPath + "start_date_5.png")
        self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_mashupcontainer-170_timeselector-179"]/div/div[1]/div/div[3]').click()
        sleep(3)
        self.driver.save_screenshot(testDirPath + "end_date_6.png")
        
    def refresh_btn(self):
        self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_mashupcontainer-170_timeselector-179"]/div/div[1]/div/div[2]').click()
        sleep(3)
        self.driver.save_screenshot(testDirPath + "Refresh_togglr_button_7.png")
        self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_mashupcontainer-170_timeselector-179"]/div/div[2]/div[3]').click()
        sleep(3)
        
    def checkbox(self):
        self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_mashupcontainer-170_clickablecontainermashup-191_ptcscheckbox-28"]').click()
        sleep(3)
        self.driver.save_screenshot(testDirPath + "HideDetails_checkbox_8.png")
        self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_mashupcontainer-170_clickablecontainermashup-191_ptcscheckbox-29"]').click()
        sleep(3)
        self.driver.save_screenshot(testDirPath + "show_sub_status_checkbox_9.png")

    def screenshot_on_failure(self):
        attach(data=self.driver.get_screenshot_as_png())
        
if __name__ == "__main__":
    unittest.main()
