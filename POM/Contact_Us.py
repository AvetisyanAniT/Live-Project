from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Lib import LIB

class Contact_Us:

    #locators
    subject_heading = (By.ID, "id_contact")
    email_address = (By.ID, "email")
    order_reference = (By.NAME, "id_order")
    attach_file = (By.ID, "fileUpload")
    input_message_text = (By.ID, "message")
    send_btn = (By.ID, "submitMessage")
    success_message = (By.CSS_SELECTOR, "p[class='alert alert-success']")
    error_message = (By.XPATH, "//div[@class='alert alert-danger']//li")

    #methods
    def __init__(self, browser):
        self.browser = browser

    #choose_subject_heading
    def choose_subject_heading(self, browser):
        LIB.wait_for_element(self, browser, self.email_address)
        select_text = LIB.get_data(self, key = 'subject_heading2')
        element = self.browser.find_element(*self.subject_heading)
        element.click()
        select = Select(element)
        select.select_by_visible_text(select_text)

    #input email address
    def input_email_address(self):
        email_value = LIB.get_data(self, key = 'valid_email')
        self.browser.find_element(*self.email_address).send_keys(email_value)
    
    #select order reference
    # def choose_order_reference(self):
    #     select = Select(self.browser.find_element(*self.order_reference))
    #     select.select_by_value('0')

    #input message
    def input_message(self):
        message = LIB.get_data(self, key = 'contact_us_input_message')
        self.browser.find_element(*self.input_message_text).send_keys(message)

    #clcik Send button
    def click_send_button(self):
        self.browser.find_element(*self.send_btn).click()