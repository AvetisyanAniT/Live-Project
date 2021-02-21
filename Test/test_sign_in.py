from selenium import webdriver
from Lib import LIB
from POM.Home import Home
from POM.Sign_in import Sign_in
import json
import pytest

def test_1():
   
    try:
        #open browser
        obj_lib = LIB()
        browser = obj_lib.open_browser()
        #email_address = obj_lib.config_data(['eMail'])
        #password = obj_lib.config_data(['password'])

        #navigate to url
        obj_lib.page_load(browser)

        #create Home page object
        obj_home = Home(browser)

        #click on Sign in
        browser.find_element(*obj_home.sign_in).click()

        #create Sign in object
        obj_signin = Sign_in(browser)

        #submit wit email and pass
        obj_lib.wait_for_element(browser, obj_signin.email_address)
        browser.find_element(*obj_signin.email_address).send_keys('aniavetisyan1997@gmail.com')
        browser.find_element(*obj_signin.password).send_keys('test112233')

        #click on Sign in button
        browser.find_element(*obj_signin.sign_in_btn).click()

        #check that we are in My Account page
        browser.find_element(*obj_signin.my_account_title)

        print("Test run pass!")

    # except Exception as e:
    #     print(e)
    #     obj_lib.save_screenshot(browser)
    #     print("Test run failed!")

    finally:
        #close browser
        obj_lib.close_browser(browser)

# test_1()
