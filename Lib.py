from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import json
import os
import sys

class LIB:

    def __init__(self):
        self.config_data = self.load_config()
    
    def load_config(self):
        with open('config.json') as f:
            data = json.load(f)
        return data    

    #create Chrome driver
    def open_browser(self):
        try:
            browser = webdriver.Chrome(self.config_data['driver_path'])
            browser.maximize_window()
            return browser
        except:
            print('Smth went wrong during browser opening!')
            
    #navigate to given url-path
    def page_load(self, browser):
        try:
           browser.get(self.config_data['url'])
        except:
            print('Smth went wrong with page load!')
    
    #open txt file with log name and write there given text
    def write_to_file(self, text):
        try:
            with open('log.txt', 'a') as file:
                return file.write('\n' + str(text))
        except:
            print('Error during writnig to file!')

    #move to given element
    def move_to_element(self, browser, element):
        try:
            action = ActionChains(browser)
            action.move_to_element(element).perform()
        except:
            print('Can not move to given element!')
    
    #wait for given element to be visible in UI
    def wait_for_element(self, browser, element):
        try:
            WebDriverWait(browser, 10).until(EC.visibility_of_element_located(element))
        except:
            print('Element is not visible!')
        
    #wait for given elements to be visible in UI
    def wait_for_elements(self, browser, elements):
        try:
            WebDriverWait(browser, 10).until(EC.visibility_of_any_elements_located(element))
        except:
            print('Elements are not visible!')

    #data parsing
    def get_data(self, key):
        try:
            with open('data.json') as f:
                data = json.load(f)
            return data[key]
        except:
            print('Error during data getting!')

    #save screenshot    
    def save_screenshot(self, browser):
        current_filename = os.path.basename(sys.argv[0][:-3])
        try:
            browser.save_screenshot(f'Test\\{current_filename}_screenshot.png')
        except:
            print('Screenshot is not saved!')

    #close browser
    def close_browser(self, browser):
        try:
            browser.quit()
        except:
            print('Browser is not closed!') 