import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    # Set preferences
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(3)
    browser.maximize_window()

    # Yield browser with set preferences
    yield browser

    # Close browser after the test
    browser.quit()
