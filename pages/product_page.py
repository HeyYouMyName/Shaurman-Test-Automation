from selenium.webdriver.common.by import By

from pages.base_page import BasePage

PRICE_ON_PRODUCT_PAGE = (By.CSS_SELECTOR, "div.single-product__content > div.single-product__order > p > span")


class ProductPage(BasePage):
    # Locators
    PRICE_ON_PRODUCT_PAGE = (By.CSS_SELECTOR, "div.single-product__content > div.single-product__order > p > span")

    def check_price_equal_product(self):
        price_product = self.browser.find_element(*self.PRICE_ON_PRODUCT_PAGE).text
        return price_product
