from utilities.Pages.home_page import HomePageSearchProduct
import logging
import time

from utilities.Pages.Base_Page import BasePage
import utilities.utils.custom_logger as cl


class AddToCart(BasePage):
    """
    Searching products in Amazon
    """
    log = cl.customLogger(logging.DEBUG)
    __add_to_cart_button = "wishListMainButton-announce"

    # def __add_to_cart(self):
    #     return self.getElement("add-to-cart-button",locatorType="id")

    def __init__(self, driver):
        # We are inheriting GenericMethods for webdriver(driver) using super() -->parameterized constructor
        super().__init__(driver)
        self.driver = driver
        HomePageSearchProduct(driver)

    def click_on_add_to_cart(self):
        self.switch_to_child_window(self.driver)
        self.elementClick(self.__add_to_cart_button)
        self.timeSleep()
