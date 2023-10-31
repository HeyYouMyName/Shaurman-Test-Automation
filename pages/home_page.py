from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    # Locators
    SLIDER = (By.CSS_SELECTOR, "div.slider-block")

    def check_slider_present(self) -> None:
        assert self._is_element_visible(*self.SLIDER)

    def check_that_you_are_back_on_home_page(self) -> None:
        current_url = self.browser.current_url
        assert "https://shaurman.com.ua/" == current_url
