from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class GoogleMapsPage(BasePage):
    # Locators
    ADDRESS_OF_SHAURMAN_ON_GOOGLE_MAPS = (By.CSS_SELECTOR, '[aria-label="\'Одеса, вул. Преображенська, 36\'"]')

    def check_address_on_maps_page_equals_to_shaurman(self, note_address_text) -> None:
        self._is_element_clickable(*self.ADDRESS_OF_SHAURMAN_ON_GOOGLE_MAPS)
        address_on_google_maps = self.browser.find_element(*self.ADDRESS_OF_SHAURMAN_ON_GOOGLE_MAPS)
        address_on_google_maps_text = address_on_google_maps.get_attribute("aria-label")[1:-1]
        assert note_address_text == address_on_google_maps_text
