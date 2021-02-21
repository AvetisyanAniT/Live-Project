from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Lib import LIB

class Sign_in:

    #locators
    email_address = (By.ID, "email")
    password = (By.ID, "passwd")
    sign_in_btn = (By.ID, "SubmitLogin")
    my_account_title = (By.CSS_SELECTOR, "h1[class='page-heading']")

    #init
    def __init__(self, browser):
        self.browser = browser