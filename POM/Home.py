from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from Lib import LIB

class Home:

    #locators
    sign_in = (By.CSS_SELECTOR, "a[title='Log in to your customer account']")
    contact_us = (By.CSS_SELECTOR, "a[title='Contact Us']")
    logo = (By.ID, "header_logo")
    women_tab = (By.CSS_SELECTOR, "a[title='Women']")
    dresses_tab = (By.XPATH, "(//div[@id='block_top_menu']//following::a[@title='Dresses'])[2]")
    t_shirt_tab = (By.XPATH, "(//div[@id='block_top_menu']//following::a[@title='T-shirts'])[2]")
    cart = (By.CSS_SELECTOR, "a[title = 'View my shopping cart']")
    search_input = (By.ID, "search_query_top")
    search_bin = (By.NAME, "submit_search")
    product_name = (By.XPATH, "//ul[@class='product_list grid row homefeatured tab-pane active']//div[@class='right-block']//a[@title = 'Faded Short Sleeve T-shirts']")
    product_price = (By.XPATH, "//p[@class='product-desc']//following::span[@class='price product-price']")
    add_to_cart_btn = (By.XPATH, "//div[@class='button-container']//span[text()='Add to cart']")
    close_popup_icon = (By.CSS_SELECTOR, "span[title='Close window']")
    pop_up_success_message = (By.XPATH, "(//div[@id='layer_cart']//h2)[1]")

    def __init__(self, browser):
        self.browser = browser

    #click Contact Us
    def click_contact_us(self, browser):
        LIB.wait_for_element(self, browser, self.contact_us)
        self.browser.find_element(*self.contact_us).click()

    #return product name:price list
    def give_product_name_price(self, browser):
        product_name_list = []
        product_price_list = []
        LIB.wait_for_element(self, browser, self.product_name)
        product_name = self.browser.find_element(*self.product_name)
        for i in product_name:
            product_name_list.append(i.text)
        product_price = self.browser.find_element(*self.product_price)
        for i in product_price:
            product_price_list.append(i.text)
        del product_price_list[1::2] #delete every second element
        return dict(zip(product_name_list, product_price_list))