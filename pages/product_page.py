from selenium.webdriver.common.by import By

from pages.base_page import BasePage




class ProductPage(BasePage):
    # Locators
    PRICE_ON_PRODUCT_PAGE = (By.CSS_SELECTOR, "div.single-product__content > div.single-product__order > p > span")

    def get_price_on_product(self):
        price_product = self.browser.find_element(*self.PRICE_ON_PRODUCT_PAGE).text
        return price_product
