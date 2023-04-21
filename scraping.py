from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time

class ScrapScrap:

    def __init__(self,chrome_path, options=None):
        self.driver = webdriver.Chrome(chrome_path)

    def get(self, url):
        self.driver.get(url)

    def refresh(self):
        self.driver.refresh()

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def wait(self, element):
        time.sleep(20)

    def maximize(self):
        self.driver.maximize_window()

    def find_xpath(self, xpath, operation, element=None):
        if operation == "click":
            self.driver.find_element_by_xpath(xpath).click()
        elif operation == "send":
            self.driver.find_element_by_xpath(xpath).send_keys(element)
        elif operation == "enter":
            self.driver.find_element_by_xpath(xpath).enter()
        elif operation == "text":
            return self.driver.find_element_by_xpath(xpath).text
        elif operation == "find":
            return self.driver.find_element_by_xpath(xpath)
        
    def find_all_xpath(self, xpath, operation, element=None):
        if operation == "click":
            self.driver.find_elements_by_xpath(xpath).click()
        elif operation == "send":
            self.driver.find_elements_by_xpath(xpath).send_keys(element)
        elif operation == "enter":
            self.driver.find_elements_by_xpath(xpath).enter()
        elif operation == "find":
            return self.driver.find_elements_by_xpath(xpath)
        