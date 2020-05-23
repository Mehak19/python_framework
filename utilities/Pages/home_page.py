import logging
import time

from utilities.Pages.Base_Page import BasePage
import utilities.utils.custom_logger as cl


class HomePageSearchProduct(BasePage):
    """
    Searching products in Amazon
    """
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        # We are inheriting GenericMethods for webdriver(driver) using super() -->parameterized constructor
        super().__init__(driver)
        self.driver = driver
        self.search_Product_Name = "twotabsearchtextbox"

    def SearchBox(self, productName):
        # using self keyword we can access the methods in generic_methods
        self.sendKeys(productName, self.search_Product_Name)
        # self.elementClick("//span[@id='nav-search-submit-text']/../input",locatorType='xpath')
        self.elementClick("//input[@value='Go']", "xpath")
        time.sleep(3)

    def click_on_product(self):
        # self.switch_to_child_window(self.driver)
        self.elementClick("//span[text()='R. Nageswara Rao']/..//preceding-sibling::h2/a", "xpath")
        self.timeSleep()
