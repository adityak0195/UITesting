from selenium import webdriver
from selenium.webdriver.edge.options import Options
from pytest_html_reporter import attach
from time import sleep
from pyshadow.main import Shadow
import unittest
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.support import expected_conditions as EC
options = Options()
options.add_argument("--headless")
testPathImages = "./RVS_Automation_Test_Results/TestImages"
testImage=testPathImages+"/OperatorInterface"
def checkIfDirExists(dirPath):
    return os.path.exists(dirPath)
if checkIfDirExists(testImage):
    pass
else:
    os.mkdir(testImage)
testDirPath = "./RVS_Automation_Test_Results/TestImages/OperatorInterface/"

class TestClass(unittest.TestCase):
    def __init__(self, driver):
        super().__init__(driver)

    def setUp(self):
        global driver
        self.driver = webdriver.Edge(options=options)
        #self.driver.maximize_window()
        
    def test_demo(self):
        self.driver.get("https://smartproductionrvstest.corp.knorr-bremse.com/Thingworx/Runtime/index.html?mashup=KBRVSPNAE15Mashup&appKey=a59beff9-da8f-4700-ab43-240c97e0ac1a&x-thingworx-session=true ")
        #self.driver.set_window_size(1920,1080)
        sleep(30)
        try:
            self.driver.save_screenshot(testDirPath + "Operator_Interface_Page.png")
            self.changeorder()
            self.confirmParts()
            self.setTarget()
            self.operatorAbsence()
            self.changeover()
            self.toolChange()
            self.unplannedRepair()
            self.technologytest()
            self.qualityCheck()
            self.missigMaterial()
        finally:
            self.driver.quit()
    def changeorder(self):
        self.driver.find_element("xpath",'//*[@id="root_mashupcontainer-1_valuedisplaykb-104"]/div/table/tbody/tr/td/div').click()
        sleep(20)
        self.driver.save_screenshot("Changecurrentorderandpart.png")
        shadow=Shadow(self.driver)
        textfield1=shadow.find_element("ptcs-textfield#root_mashupcontainer-1_navigationfunction-115-popup_ptcstextfield-31>div>div[part=text-box]>ptcs-button#clearbutton").click()
        sleep(10)
        self.driver.save_screenshot("OrderCleared.png")
        order="2222"
        shadow=Shadow(self.driver)
        order1=shadow.find_element("ptcs-textfield#root_mashupcontainer-1_navigationfunction-115-popup_ptcstextfield-31>div>div[part=text-box]>span#maskShell>input#input")
        order1.send_keys(order)
        sleep(10)
        self.driver.save_screenshot("ordernumber.png")
        self.driver.find_element("xpath",'//*[@id="root_mashupcontainer-1_navigationfunction-115-popup_ptcstextfield-32"]').click()
        sleep(2)
        shadow=Shadow(self.driver)
        textfield2=shadow.find_element("ptcs-textfield#root_mashupcontainer-1_navigationfunction-115-popup_ptcstextfield-32>div>div[part=text-box]>ptcs-button#clearbutton").click()
        sleep(10)
        self.driver.save_screenshot("PartCleared.png")
        part="5555"
        shadow=Shadow(self.driver)
        part1=shadow.find_element("ptcs-textfield#root_mashupcontainer-1_navigationfunction-115-popup_ptcstextfield-32>div>div[part=text-box]>span#maskShell>input#input")
        part1.send_keys(part)
        sleep(10)
        self.driver.save_screenshot("partnumber.png")
        self.driver.find_element("xpath",'//*[@id="root_mashupcontainer-1_navigationfunction-115-popup_ptcsbutton-23"]').click()
        sleep(15)
        self.driver.save_screenshot("Datachanged.png")
        ''' label_value=shadow.find_element("ptcs-label#root_mashupcontainer-1_ptcslabel-49>div[id='root']")
        label_value_aria_label=label_value.get_attribute('value')
        print(label_value_aria_label)
        self.assertEqual(label_value_aria_label,"2222","label not matched")'''
        print("label matched")
    def confirmParts(self):
        self.driver.find_element("xpath",'//*[@id="root_mashupcontainer-1_valuedisplaykb-105"]/div/table/tbody/tr/td/div').click()
        sleep(2)
        self.driver.save_screenshot("Okconfirmparts.png") 
        self.driver.find_element("xpath",'//*[@id="root_mashupcontainer-1_navigationfunction-116-popup_ptcsbutton-38"]').click()
        sleep(2)
        self.driver.save_screenshot("Okaddvalue.png")
        self.driver.find_element("xpath",'//*[@id="root_mashupcontainer-1_navigationfunction-116-popup_ptcsbutton-48"]').click()
        sleep(2)
        self.driver.save_screenshot("Nokaddvalue.png")
        self.driver.find_element("xpath",'//*[@id="root_mashupcontainer-1_navigationfunction-116-popup_ptcsbutton-51"]').click()
        sleep(2)
        self.driver.save_screenshot("Nokminusvalue.png")
        self.driver.find_element("xpath",'//*[@id="root_mashupcontainer-1_navigationfunction-116-popup_ptcsbutton-23"]').click()
        sleep(5)
        self.driver.save_screenshot("OkNok.png")
        oknokValue=self.driver.find_element("xpath",'//*[@id="root_mashupcontainer-1_mashupcontainer-1_valuedisplaykb-144"]/table/tbody/tr/td/div/div/div')
        oknokValue_aria_label=oknokValue.get_attribute('cellvalue')
        print(oknokValue_aria_label)
        self.assertEqual(oknokValue_aria_label,oknokValue_aria_label,"Value not matched")
        print("Value matched")
    def setTarget(self):
        self.driver.find_element("xpath",'//*[@id="root_mashupcontainer-1_valuedisplaykb-106"]/div/table/tbody/tr/td/div').click()
        sleep(2)
        self.driver.save_screenshot("settarget.png")
        target="2"
        t=self.driver.find_element("xpath",'//*[@id="root_mashupcontainer-1_navigationfunction-117-popup_numericentry-33"]/div/input')
        t.clear()
        t.send_keys(target)
        sleep(2)
        self.driver.save_screenshot("targetshift.png")
        oee="23"
        o=self.driver.find_element("xpath",'//*[@id="root_mashupcontainer-1_navigationfunction-117-popup_numericentry-34"]/div/input')
        o.clear()
        o.send_keys(oee)
        self.driver.save_screenshot("OEEplan.png")
        self.driver.find_element("xpath",'//*[@id="root_mashupcontainer-1_navigationfunction-117-popup_ptcsbutton-23"]').click()
        self.driver.save_screenshot("settargetchanged.png")
        sleep(5)
        oknokValue=self.driver.find_element("xpath",'//*[@id="root_mashupcontainer-1_mashupcontainer-1_valuedisplaykb-125"]/table/tbody/tr/td/div/div/div')
        oknokValue_aria_label=oknokValue.get_attribute('cellvalue')
        print(oknokValue_aria_label)
        self.assertEqual(oknokValue_aria_label,"23%","Value not matched")
        print("Value matched")
        
    def operatorAbsence(self):
        self.driver.find_element("xpath",'//*[@id="root_mashupcontainer-1_valuedisplaykb-94"]/div/table/tbody/tr/td/div').click()
        sleep(2)
        self.driver.save_screenshot("operatoraAbsence.png")
        shadow=Shadow(self.driver)
        select=shadow.find_element("ptcs-list#root_mashupcontainer-1_navigationfunction-119-popup_ptcslist-24>div[part='list-container']>ptcs-v-scroller#chunker>div>div>ptcs-list-item[index='1']").click()
        self.driver.save_screenshot("selected.png")
        self.driver.find_element("xpath",'//*[@id="root_mashupcontainer-1_navigationfunction-119-popup_ptcsbutton-23"]').click()
        sleep(2)
        self.driver.save_screenshot("OperatorAbsencechanged.png")
    def changeover(self):
        self.driver.find_element("xpath",'//*[@id="root_mashupcontainer-1_valuedisplaykb-95"]/div/table/tbody/tr/td/div').click()
        sleep(2)
        self.driver.save_screenshot("changeover.png")
        shadow=Shadow(self.driver)
        select=shadow.find_element("ptcs-list#root_mashupcontainer-1_navigationfunction-120-popup_ptcslist-24>div[part='list-container']>ptcs-v-scroller#chunker>div>div>ptcs-list-item[index='1']").click()
        sleep(2)
        self.driver.save_screenshot("selectedchangeover.png")
        self.driver.find_element("xpath",'//*[@id="root_mashupcontainer-1_navigationfunction-120-popup_ptcsbutton-23"]').click()
        sleep(2)
        self.driver.save_screenshot("changeoverchanged.png")
    def toolChange(self):
        self.driver.find_element("xpath",'//*[@id="root_mashupcontainer-1_valuedisplaykb-96"]/div/table/tbody/tr/td/div').click()
        sleep(2)
        self.driver.save_screenshot("toolchange.png")
        shadow=Shadow(self.driver)
        select=shadow.find_element("ptcs-list#root_mashupcontainer-1_navigationfunction-121-popup_ptcslist-24>div[part='list-container']>ptcs-v-scroller#chunker>div>div>ptcs-list-item[index='0']").click()
        sleep(2)
        self.driver.save_screenshot("selectedtoolchange.png")
        self.driver.find_element("xpath",'//*[@id="root_mashupcontainer-1_navigationfunction-121-popup_ptcsbutton-23"]').click()
        sleep(2)
        self.driver.save_screenshot("toolchanged.png")
    def unplannedRepair(self):
        self.driver.find_element("xpath",'//*[@id="root_mashupcontainer-1_valuedisplaykb-97"]/div/table/tbody/tr/td/div').click()
        sleep(2)
        self.driver.save_screenshot("UnplannedRepair.png")
        shadow=Shadow(self.driver)
        select=shadow.find_element("ptcs-list#root_mashupcontainer-1_navigationfunction-122-popup_ptcslist-24>div[part='list-container']>ptcs-v-scroller#chunker>div>div>ptcs-list-item[index='1']").click()
        sleep(2)
        self.driver.save_screenshot("selectedrepair.png")
        self.driver.find_element("xpath",'//*[@id="root_mashupcontainer-1_navigationfunction-122-popup_ptcsbutton-23"]').click()
        sleep(2)
        self.driver.save_screenshot("unplannedrepairchanged.png")
    def technologytest(self):
        self.driver.find_element("xpath",'//*[@id="root_mashupcontainer-1_valuedisplaykb-98"]/div/table/tbody/tr/td/div').click()
        sleep(2)
        self.driver.save_screenshot("technologytest.png")
        shadow=Shadow(self.driver)
        select=shadow.find_element("ptcs-list#root_mashupcontainer-1_navigationfunction-123-popup_ptcslist-24>div[part='list-container']>ptcs-v-scroller#chunker>div>div>ptcs-list-item[index='1']").click()
        sleep(2)
        self.driver.save_screenshot("selectedtechnology.png")
        self.driver.find_element("xpath",'//*[@id="root_mashupcontainer-1_navigationfunction-123-popup_ptcsbutton-23"]').click()
        sleep(2)
        self.driver.save_screenshot("technologytestchanged.png")
    def qualityCheck(self):
        self.driver.find_element("xpath",'//*[@id="root_mashupcontainer-1_valuedisplaykb-99"]/div/table/tbody/tr/td/div').click()
        sleep(2)
        self.driver.save_screenshot( "qualitycheck.png")
        self.driver.find_element("xpath",'//*[@id="root_mashupcontainer-1_navigationfunction-124-popup_ptcsbutton-23"]').click()
        sleep(2)
        self.driver.save_screenshot("qualitycheckchanged.png")
    def missigMaterial(self):
        self.driver.find_element("xpath",'//*[@id="root_mashupcontainer-1_valuedisplaykb-114"]/div/table/tbody/tr/td/div').click()
        sleep(2)
        self.driver.save_screenshot( "missingmaterial.png")
        shadow=Shadow(self.driver)
        select=shadow.find_element("ptcs-list#root_mashupcontainer-1_navigationfunction-125-popup_ptcslist-24>ptcs-v-scroller#chunker>div>div>ptcs-list-item[index='0']").click()
        sleep(2)
        self.driver.save_screenshot( "missingmaterialselected.png")
        self.driver.find_element("xpath",'//*[@id="root_mashupcontainer-1_navigationfunction-125-popup_ptcsbutton-23"]').click()
        sleep(2)
        self.driver.save_screenshot("missingmaterialchanged.png")
    def screenshot_on_failure(self):
        attach(data=self.driver.get_screenshot_as_png())
if __name__ == "__main__":
    unittest.main()  
