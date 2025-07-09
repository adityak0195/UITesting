from selenium import webdriver
from selenium.webdriver.edge.options import Options
from pytest_html_reporter import attach
from time import sleep
from pyshadow.main import Shadow
from PIL import Image
import unittest
import os

options = Options()
options.add_argument("--headless")
testPathImages = "./RVS_Automation_Test_Results/TestImages"
testImage=testPathImages+"/MicroelectricaPrinterAssignment"
def checkIfDirExists(dirPath):
    return os.path.exists(dirPath)
 
if checkIfDirExists(testImage):
    pass
else:
    os.mkdir(testImage)
testDirPath = "./RVS_Automation_Test_Results/TestImages/MicroelectricaPrinterAssignment/"
class TestClass(unittest.TestCase):
    def __init__(self, driver):
        super().__init__(driver)

    def setUp(self):        
        global driver
        self.driver = webdriver.Edge(options=options)
        #self.driver.maximize_window()
        
    def test_demo(self):
        self.driver.get("https://smartproductionrvstest.corp.knorr-bremse.com/Thingworx/Mashups/KBPrinterSationMashup?appKey=a59beff9-da8f-4700-ab43-240c97e0ac1a&x-thingworx-session=true")
        try:
            sleep(20)
            #self.driver.set_window_size(1920,1080)
            sleep(30)
            self.driver.save_screenshot(testDirPath +"MicroelectricaPrinterAssignmentPage.png")
            self.dropdowns()
            self.adddata()
            self.editdata()
            self.deletedata()
        finally:
            self.driver.quit()
			
    def dropdowns(self):
        self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_ptcsdropdown-6"]').click()
        sleep(5)
        self.driver.save_screenshot(testDirPath +"workstation_dropdown_button.png")
        shadow=Shadow(self.driver)
        workstation_root=shadow.find_element("ptcs-list#root_pagemashupcontainer-5_ptcsdropdown-6-external-wc>div[part='list-container']>ptcs-v-scroller#chunker>div>div>ptcs-list-item[index='1']").click()
        sleep(15)
        self.driver.save_screenshot(testDirPath +"workstation_selected.png")
        workstation_dropdown_value=shadow.find_element("ptcs-dropdown#root_pagemashupcontainer-5_ptcsdropdown-6>ptcs-hbar#select>ptcs-list-item[part='list-item']")
        workstation_dropdown_value_aria_label=workstation_dropdown_value.get_attribute('aria-label')
        self.assertEqual(workstation_dropdown_value_aria_label,"KBRVSMILSwsL3TestBenchStationThing","Workstation not matched")
        print("Workstation matched")
        self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_ptcsdropdown-18"]').click()
        sleep(5)
        self.driver.save_screenshot(testDirPath +"printers_dropdown.png")
        shadow=Shadow(self.driver)
        printer_root=shadow.find_element("ptcs-list#root_pagemashupcontainer-5_ptcsdropdown-18-external-wc>div[part='list-container']>ptcs-v-scroller#chunker>div>div>ptcs-list-item[index='2']").click()
        sleep(15)
        self.driver.save_screenshot(testDirPath +"Printer_selected.png")
        printer_dropdown_value=shadow.find_element("ptcs-dropdown#root_pagemashupcontainer-5_ptcsdropdown-18>ptcs-hbar#select>ptcs-list-item[part='list-item']")
        printer_dropdown_value_aria_label=printer_dropdown_value.get_attribute('aria-label')
        self.assertEqual(printer_dropdown_value_aria_label,'KBRVSMILZebraPrinterA6MILP4064KBLabelPrinterFtpThing',"Printer not matched")
        print("Printer matched")
    def adddata(self):
        self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_ptcsbutton-19"]').click()
        sleep(10)
        self.driver.save_screenshot(testDirPath +"Dataadd.png")
        self.driver.find_element("xpath",'//*[@id="radio0"]').click()
        sleep(15)
        self.driver.save_screenshot(testDirPath +"Printer_select.png")
        shadow=Shadow(self.driver)
        printer_textfield=shadow.find_element("ptcs-textfield#root_pagemashupcontainer-5_navigationfunction-22-popup_ptcstextfield-6>div[part='root']>div[part='text-box']>span[class='shell']>input[part='text-value']")
        printer_textfield_value=printer_textfield.get_attribute('value')
        self.assertEqual(printer_textfield_value,'ZebraPrinterSMALLMILP',"printer not matched")
        print("Printer matched")
        IP="1101010100"
        a=self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_navigationfunction-22-popup_ptcstextfield-8"]')
        a.send_keys(IP)
        sleep(5)
        self.driver.save_screenshot(testDirPath +"Ip_entered.png")
        ip_textfield=shadow.find_element("ptcs-textfield#root_pagemashupcontainer-5_navigationfunction-22-popup_ptcstextfield-8>div[part='root']>div[part='text-box']>span[class='shell']>input[part='text-value']")
        ip_textfield_value=ip_textfield.get_attribute('value')
        self.assertEqual(ip_textfield_value,'1101010100',"IP not matched")
        print("IP matched")
        self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_navigationfunction-22-popup_ptcsbutton-9"]').click()
        sleep(15)
        self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_navigationfunction-22-popup"]/div[1]/span[2]').click()
        sleep(5)
        self.driver.save_screenshot(testDirPath +"create_printer.png")
        
    def editdata(self):
        self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_ptcsbutton-8"]').click()
        sleep(5)
        self.driver.save_screenshot(testDirPath +"Edit_data.png")
        self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_navigationfunction-10-popup_ptcsdropdown-21"]').click()
        sleep(5)
        self.driver.save_screenshot(testDirPath +"Workstation_dropdown.png")
        shadow=Shadow(self.driver)
        workstationroot=shadow.find_element("ptcs-list#root_pagemashupcontainer-5_navigationfunction-10-popup_ptcsdropdown-21-external-wc>div[part='list-container']>ptcs-v-scroller#chunker>div>div>ptcs-list-item[index='2']").click()
        sleep(5)
        self.driver.save_screenshot(testDirPath +"Workstation_Created.png")
        workstation_dropdown_value=shadow.find_element("ptcs-dropdown#root_pagemashupcontainer-5_navigationfunction-10-popup_ptcsdropdown-21>ptcs-hbar#select>ptcs-list-item[part='list-item']")
        workstation_dropdown_value_aria_label=workstation_dropdown_value.get_attribute('aria-label')
        self.assertEqual(workstation_dropdown_value_aria_label,"KBMUCZebraPrinterSMALLMILPKBLabelPrinterFtpThing","Workstation not matched")
        print("Workstation matched")
        self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_navigationfunction-10-popup_ptcsdropdown-3"]').click()
        sleep(5)
        self.driver.save_screenshot(testDirPath +"Labelprinter_dropdown.png")
        shadow=Shadow(self.driver)
        labelprinterroot=shadow.find_element("ptcs-list#root_pagemashupcontainer-5_navigationfunction-10-popup_ptcsdropdown-3-external-wc>div[part='list-container']>ptcs-v-scroller#chunker>div>div>ptcs-list-item[index='1']").click()
        sleep(5)
        self.driver.save_screenshot(testDirPath +"Labelprinter_selected.png")
        label_printer_dropdown_value=shadow.find_element("ptcs-dropdown#root_pagemashupcontainer-5_navigationfunction-10-popup_ptcsdropdown-3>ptcs-hbar#select>ptcs-list-item[part='list-item']")
        label_printer_dropdown_value_aria_label=label_printer_dropdown_value.get_attribute('aria-label')
        self.assertEqual(label_printer_dropdown_value_aria_label,"KBRVSMILZebraPrinterSMALLMILP4031KBLabelPrinterFtpThing","LabelPrinter not matched")
        print("label Printer matched")
        self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_navigationfunction-10-popup_ptcsdropdown-10"]').click()
        sleep(5)
        self.driver.save_screenshot(testDirPath +"Packagingprinter_dropdown.png")
        shadow=Shadow(self.driver)
        root6=shadow.find_element("ptcs-list#root_pagemashupcontainer-5_navigationfunction-10-popup_ptcsdropdown-10-external-wc>div[part='list-container']>ptcs-v-scroller#chunker>div>div>ptcs-list-item[index='0']").click()
        sleep(5)
        self.driver.save_screenshot(testDirPath +"Packagingprinter_selected.png")
        packaging_printer_dropdown_value=shadow.find_element("ptcs-dropdown#root_pagemashupcontainer-5_navigationfunction-10-popup_ptcsdropdown-10>ptcs-hbar#select>ptcs-list-item[part='list-item']")
        packaging_printer_dropdown_value_aria_label=packaging_printer_dropdown_value.get_attribute('aria-label')
        self.assertEqual(packaging_printer_dropdown_value_aria_label,"KBRVSMILZebraPrinterA6MILP4064KBLabelPrinterFtpThing","packaging not matched")
        print("Packaging Printer matched")
        self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_navigationfunction-10-popup_ptcscheckbox-6"]').click()
        sleep(5)
        self.driver.save_screenshot(testDirPath +"Labelprinter_checkbox.png")
        self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_navigationfunction-10-popup_ptcscheckbox-12"]').click()
        sleep(5)
        self.driver.save_screenshot(testDirPath +"packagingprinter_checkbox.png")
        self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_navigationfunction-10-popup_ptcsbutton-15"]').click()
        sleep(5)
        self.driver.save_screenshot(testDirPath +"Dataedited.png")
    def deletedata(self):
        self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_ptcsbutton-20"]').click()
        sleep(5)
        self.driver.save_screenshot(testDirPath +"Deleteprinter.png")
        self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_navigationfunction-21-popup_ptcsdropdown-12"]').click()
        sleep(5)
        self.driver.save_screenshot(testDirPath +"Printer_dropdown.png")
        shadow=Shadow(self.driver)
        printer_root=shadow.find_element("ptcs-list#root_pagemashupcontainer-5_navigationfunction-21-popup_ptcsdropdown-12-external-wc>div[part='list-container']>ptcs-v-scroller#chunker>div>div>ptcs-list-item[index='2']").click()
        sleep(5) 
        self.driver.save_screenshot(testDirPath +"printer_selected.png")
        printer_dropdown_value=shadow.find_element("ptcs-dropdown#root_pagemashupcontainer-5_navigationfunction-21-popup_ptcsdropdown-12>ptcs-hbar#select>ptcs-list-item[part='list-item']")
        printer_dropdown_value_aria_label=printer_dropdown_value.get_attribute('aria-label')
        self.assertEqual(printer_dropdown_value_aria_label,"KBRVSMILZebraPrinterSMALLMILP4031KBLabelPrinterFtpThing","Printer not matched")
        print("Printer matched")
        self.driver.find_element("xpath",'//*[@id="root_pagemashupcontainer-5_navigationfunction-21-popup_ptcsbutton-13"]')
        self.driver.save_screenshot(testDirPath +"Printerdeleted.png")



    def screenshot_on_failure(self):
        attach(data=self.driver.get_screenshot_as_png())
if __name__ == "__main__":
    unittest.main()  
