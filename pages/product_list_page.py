from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductListPage(BasePage):
    # Locators
    CHANGE_BUTTON = (By.CSS_SELECTOR, ".btn-green")
    ORDER_BUTTON = (By.CSS_SELECTOR, ".btn-red")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".products__item-head .products__item-title")
    PRODUCT_WEIGHT = (By.CSS_SELECTOR, ".products__item-head .products__item-weight")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".products__item-head .products__item-price")
    PRODUCT_INGREDIENTS = (By.CSS_SELECTOR, ".products__item-head .products__item-description")
    PRODUCT_IMG = (By.CSS_SELECTOR, ".products__item-thumb")

    def check_change_button_present(self) -> None:
        assert self._is_elements_visible(*self.CHANGE_BUTTON)

    def check_product_title_weight_price_ingredients_present(self) -> None:
        assert self._is_elements_visible(*self.PRODUCT_TITLE)
        assert self._is_elements_visible(*self.PRODUCT_WEIGHT)
        assert self._is_elements_visible(*self.PRODUCT_PRICE)
        assert self._is_elements_visible(*self.PRODUCT_INGREDIENTS)

    def check_order_button_present(self) -> None:
        assert self._is_elements_visible(*self.ORDER_BUTTON)

    def click_on_change_button(self, arg):
        side_bar_menu = self.browser.find_elements(*self.CHANGE_BUTTON)
        side_bar_menu[arg].click()

    def click_on_order_button(self, arg):
        side_bar_menu = self.browser.find_elements(*self.ORDER_BUTTON)
        side_bar_menu[arg].click()

    def get_hold_of_price(self, arg):
        price = self.browser.find_elements(*self.PRODUCT_PRICE)[arg].text
        return price

    def click_on_image_and_go_to_product_page(self, arg):
        self.browser.find_elements(*self.PRODUCT_IMG)[arg].click()

