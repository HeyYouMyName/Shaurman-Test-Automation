from selenium.common import TimeoutException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def check_prices_are_equal(val1, val2):
    assert val1 == val2, "they are not equal"


class BasePage:
    URL = r"https://shaurman.com.ua/"

    # Locators
    SIDEBAR_BLOCK = (By.CSS_SELECTOR, "div.sidebar")
    TOP_BAR_BLOCK = (By.CSS_SELECTOR, "div.top-menu")

    FOOTER_CONTAINER = (By.CSS_SELECTOR, "div.footer__container")
    MAIN_CONTENT_BLOCK = (By.CSS_SELECTOR, "#content.main")

    SIDEBAR_ITEMS = (By.CSS_SELECTOR, f"div.sidebar > ul:nth-child(2) > li")

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
