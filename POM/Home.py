from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from Lib import LIB

class Home:

    #locators
    sign_in = (By.CSS_SELECTOR, "a[title='Log in to your customer account']")
    contact_us = (By.CSS_SELECTOR, "a[title='Contact Us']")

    def __init__(self, browser):
        self.browser = browser

    def click_contact_us(self, browser):
        LIB.wait_for_element(self, browser, self.contact_us)
        self.browser.find_element(*self.contact_us).click()