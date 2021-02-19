from selenium import webdriver
from Lib import LIB
from POM.Home import Home
from POM.Contact_Us import Contact_Us
import json
import pytest

def test_2():
    
    try:
        #open browser
        obj_lib = LIB()
        browser = obj_lib.open_browser()

        #navigate to url
        obj_lib.page_load(browser)

        #create contact_us object
        obj_contact_us = Contact_Us(browser)

        #create Home page object
        obj_home = Home(browser)

        #stepts
        obj_home.click_contact_us(browser)
        obj_contact_us.choose_subject_heading(browser)
        obj_contact_us.input_email_address()
        # obj_contact_us.choose_order_reference()
        obj_contact_us.input_message()
        obj_contact_us.click_send_button()

        #verify that message is sending successfully
        success_message = obj_lib.get_data('contact_us_success_message')
        message_text = browser.find_element(*obj_contact_us.success_message).text
        assert success_message in message_text, obj_lib.save_screenshot(browser)

        print("Test run pass!")

    # except Exception as e:
    #     print(e)
    #     obj_lib.save_screenshot(browser)
    #     print("Test run failed!")

    finally:
        #close browser
        obj_lib.close_browser(browser)

# test_2()