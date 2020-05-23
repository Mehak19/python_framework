from test_scripts.test_cases.test_amazon import Amazon
from utilities.utils import excel
import pytest


@pytest.mark.usefixtures("oneTimeSetUp")
class Test_AmazonProj():

    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.hs = Amazon(self.driver)

    @pytest.mark.run(order=1)
    def test_tc_001_add_product_and_verify(self):
        product_name = excel.get_value("sheet", "TC001", "Product")
        self.hs.searchProduct(product_name)
        # success_message = excel.get_value("sheet", "TC001", "SuccessMessage")
        # success_message_after_deleting = excel.get_value("sheet", "TC001", "SuccessMessageAfterDelete")


"""
OUTPUT:
py.test  -v -s test_runner.py --browser firefox
py.test  -v -s test_runner.py --browser chrome


TO GENERATE HTML REPORT :
PREREQUISITE: 
        pip install pytest-HTML



TO GENERATE A REPORT : 
TO GENERATE A REPORT : 
py.test -x testrunner_.py --browser chrome --html=Amazon_searchProduct.html
"""
