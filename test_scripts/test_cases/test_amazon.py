from utilities.Pages.home_page import HomePageSearchProduct as searchProd
from utilities.Pages.add_to_cart import AddToCart
from source.generic_utils.webdriverfactory import WebDriverFactory


# Searching the product in search box
class Amazon(WebDriverFactory):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def searchProduct(self, name):
        searchProd(self.driver).SearchBox(name)
        searchProd(self.driver).click_on_product()
        AddToCart(self.driver).click_on_add_to_cart()

    # def add_to_cart(self):
    #     AddToCart
