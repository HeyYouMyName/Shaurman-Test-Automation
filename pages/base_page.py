from selenium.common import TimeoutException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    URL = r"https://shaurman.com.ua/"

    # Locators
    SIDEBAR_BLOCK = (By.CSS_SELECTOR, "div.sidebar")
    TOP_BAR_BLOCK = (By.CSS_SELECTOR, "div.top-menu")
    FOOTER_CONTAINER = (By.CSS_SELECTOR, "div.footer__container")
    MAIN_CONTENT_BLOCK = (By.CSS_SELECTOR, "#content.main")
    SIDEBAR_ITEMS = (By.CSS_SELECTOR, f"div.sidebar > ul:nth-child(2) > li")
    LINK_ON_FOOTER_DELIVERY_AND_PAYMENT = (By.CSS_SELECTOR, "div.footer__nav > ul > li:nth-child(2) > a")
    LINK_ON_FOOTER_NEWS = (By.CSS_SELECTOR, "div.footer__nav > ul > li:nth-child(3) > a")
    LINK_ON_FOOTER_OFFERTA = (By.CSS_SELECTOR, "div.footer__nav > ul > li:nth-child(4) > a")
    ADDRESS_OF_SHAURMAN = (By.CSS_SELECTOR, "div.footer__address a")

    def __init__(
        self,
        browser: webdriver
    ):
        self.browser = browser

    def open(self) -> None:
        """
        Open a page.
        """
        self.browser.get(self.URL)

    # General methods
    def _is_element_present(
        self,
        locator: str,
        selector: str,
        timeout: int = 4
    ) -> bool:
        """
        Check if specified element is present on the page
        """
        return not self._is_not_element_present(locator, selector, timeout)

    def _is_not_element_present(
        self,
        locator: str,
        selector: str,
        timeout: int = 4
    ) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((locator, selector))
            )
        except TimeoutException:
            return True
        return False

    def _is_element_visible(
        self,
        locator: str,
        selector: str,
        timeout: int = 4
    ) -> bool:
        """
        Check if specified element is visible on the page
        """
        return not self._is_not_element_visible(locator, selector, timeout)

    def _is_elements_visible(
        self,
        locator: str,
        selector: str,
        timeout: int = 4
    ) -> bool:
        return not self._is_not_elements_visible(locator, selector, timeout)

    def _is_not_element_visible(
        self,
        locator: str,
        selector: str,
        timeout: int = 4
    ) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located((locator, selector))
            )
        except TimeoutException:
            return True
        return False

    def _is_not_elements_visible(
        self,
        locator: str,
        selector: str,
        timeout: int = 4
    ) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_all_elements_located((locator, selector))
            )
        except TimeoutException:
            return True
        return False

    def _check_url_contains(
        self,
        url_fragment: str
    ) -> bool:
        """
        Check if provided url_fragment is present in the actual.
        """
        return url_fragment in self.browser.current_url

    def scroll_to_bottom(self) -> None:
        """
        Scroll page to the very bottom.
        """
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Specific methods
    # Checks
    def check_sidebar_present(self) -> None:
        assert self._is_element_visible(*self.SIDEBAR_BLOCK)

    def check_tob_bar_present(self) -> None:
        assert self._is_element_visible(*self.TOP_BAR_BLOCK)

    def check_footer_container_present(self) -> None:
        assert self._is_element_visible(*self.FOOTER_CONTAINER)

    def check_main_content_block_present(self) -> None:
        assert self._is_element_visible(*self.MAIN_CONTENT_BLOCK)

    def click_on_sidebar_category(self, arg):
        side_bar_menu = self.browser.find_elements(*self.SIDEBAR_ITEMS)
        side_bar_menu[arg].click()

    @staticmethod
    def check_prices_are_equal(val1, val2):
        assert val1 == val2, "they are not equal"

    def _is_element_clickable(
        self,
        locator: str,
        selector: str,
        timeout: int = 4
    ) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((locator, selector)))
            return True
        except:
            return False

    def click_on_delivery_and_payment_link(self):
        link = self.browser.find_element(*self.LINK_ON_FOOTER_DELIVERY_AND_PAYMENT)
        link.get_attribute("href")
        link.click()

    def click_on_news_link(self):
        link = self.browser.find_element(*self.LINK_ON_FOOTER_NEWS)
        link.click()

    def click_on_offer_link(self):
        link = self.browser.find_element(*self.LINK_ON_FOOTER_OFFERTA)
        link.click()

    def note_the_address_and_go_to_google_maps_window(self, index):
        note_address = self.browser.find_element(*self.ADDRESS_OF_SHAURMAN)
        note_address_text = note_address.text
        note_address.click()
        self.browser.switch_to.window(self.browser.window_handles[index])
        return note_address_text

