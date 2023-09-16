from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    # Locators
    SLIDER = (By.CSS_SELECTOR, "div.slider-block")
    def check_slider_present(self) -> None:
        assert self._is_element_visible(*self.SLIDER)
