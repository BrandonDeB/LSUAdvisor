from selenium import webdriver
from selenium.webdriver.common.by import By

class AuditScraper:

    def __init__(self, webDriver):
        self.webDriver = webDriver

    def scrape(self):
        print(self.get_name())
        print(self.get_college())
        print(self.get_catalog_year())

    def get_name(self):
        fullString = self.webDriver.find_element(by=By.XPATH, value="/html/body/form/table/tbody/tr/td/div[1]").get_attribute('innerHTML')
        name = fullString.replace("Welcome, ", "")
        return name
    
    def get_college(self):
        college = self.major_and_degree()[0].get_attribute('innerHTML')
        return college

    def get_catalog_year(self):
        catalog_year = self.major_and_degree()[4].get_attribute('innerHTML')
        return catalog_year


    def major_and_degree(self):
        td_elements = self.webDriver.find_elements(by=By.CLASS_NAME, value="ReportText")
        #td_elements = td_elements.find_elements(by=By.TAG_NAME, value="td")
        filtered_list = []
        for element in td_elements:
            if element.tag_name == "td":
                filtered_list.append(element)
        return filtered_list



    

driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
driver.get("https://appl020tm.lsu.edu/stu/degreeaudit.nsf/Introduction?openForm")
scraper = AuditScraper(driver)
ready = "maybe"
while(ready!="no"):
    ready = input("Type read once logged in. Type no to stop")
    if ready == 'read':
        scraper.scrape()