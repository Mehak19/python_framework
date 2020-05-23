from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class WebDriverFactory:
    def __init__(self, driver):
        # super(WebDriverFactory, self).__init__(driver)
        self.driver = driver

    def getWebDriverInstance(self):
        if self.driver == 'firefox':
            driver = webdriver.Chrome(ChromeDriverManager().install())
        else:
            driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.amazon.in/")
        driver.implicitly_wait(10)
        return driver