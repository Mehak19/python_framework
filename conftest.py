import pytest
from source.generic_utils.webdriverfactory import WebDriverFactory
from source.generic_utils.webdriverfactory import WebDriverFactory


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
