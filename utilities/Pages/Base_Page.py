from source.generic_utils.base_utils import BaseUtils


class BasePage(BaseUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
