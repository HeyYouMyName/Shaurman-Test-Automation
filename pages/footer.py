
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Footer(BasePage):
    # Locators
    LINKS_ON_FOOTER = (By.CSS_SELECTOR, ".footer__nav .top-menu__nav li.top-menu__nav-link a")
    ADDRESS_OF_SHAURMAN = (By.CSS_SELECTOR, "div.footer__address a")
    ADDRESS_OF_SHAURMAN_ON_GOOGLE_MAPS = (By.CSS_SELECTOR, '[aria-label="\'Одеса, вул. Преображенська, 36\'"]')

    def click_on_delivery_and_payment_link(self, index) -> None:
        list_of_links = self.browser.find_elements(*self.LINKS_ON_FOOTER)
        delivery_and_payment_link_href = list_of_links[index].get_attribute("href")
        list_of_links[index].click()
        assert "delivery" in delivery_and_payment_link_href

    def click_on_news_link(self, index) -> None:
        list_of_links = self.browser.find_elements(*self.LINKS_ON_FOOTER)
        news_link_href = list_of_links[index].get_attribute("href")
        list_of_links[index].click()
        assert "blog" in news_link_href

    def click_on_offer_link(self, index) -> None:
        list_of_links = self.browser.find_elements(*self.LINKS_ON_FOOTER)
        offer_link_href = list_of_links[index].get_attribute("href")
        list_of_links[index].click()
        assert "publichnyj-dogovor-oferta" in offer_link_href

    def verifying_that_map_opens_the_correct_address(self, index) -> None:
        note_address = self.browser.find_element(*self.ADDRESS_OF_SHAURMAN)
        note_address_text = note_address.text
        note_address.click()
        self.browser.switch_to.window(self.browser.window_handles[index])
        self._is_element_clickable(*self.ADDRESS_OF_SHAURMAN_ON_GOOGLE_MAPS)
        address_on_google_maps = self.browser.find_element(*self.ADDRESS_OF_SHAURMAN_ON_GOOGLE_MAPS)
        address_on_google_maps_text = address_on_google_maps.get_attribute("aria-label")[1:-1]
        assert note_address_text == address_on_google_maps_text


