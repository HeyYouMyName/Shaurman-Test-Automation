import time

from selenium.common import TimeoutException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    URL = r"https://shaurman.com.ua/"

    # Locators
    SIDEBAR_BLOCK = (By.CSS_SELECTOR, "div.sidebar")
    TOP_BAR_BLOCK = (By.CSS_SELECTOR, "div.top-menu")
    FOOTER_CONTAINER = (By.CSS_SELECTOR, "div.footer__container")
    MAIN_CONTENT_BLOCK = (By.CSS_SELECTOR, "#content.main")
    SIDEBAR_ITEMS = (By.CSS_SELECTOR, "div.sidebar > ul:nth-child(2) > li")
    LINK_ON_FOOTER_DELIVERY_AND_PAYMENT = (By.CSS_SELECTOR, "div.footer__nav > ul > li:nth-child(2) > a")
    LINK_ON_FOOTER_NEWS = (By.CSS_SELECTOR, "div.footer__nav > ul > li:nth-child(3) > a")
    LINK_ON_FOOTER_OFFERTA = (By.CSS_SELECTOR, "div.footer__nav > ul > li:nth-child(4) > a")
    ADDRESS_OF_SHAURMAN = (By.CSS_SELECTOR, "div.footer__address a")
    LINK_ABOUT_US_TOP_BAR = (By.CSS_SELECTOR, "div.top-menu__nav-block > ul > li:nth-child(2)")
    LINK_ON_TOP_BAR_DELIVERY_AND_PAYMENT = (By.CSS_SELECTOR, "div.top-menu__nav-block > ul > li:nth-child(3)")
    LINK_ON_TOP_BAR_NEWS = (By.CSS_SELECTOR, "div.top-menu__nav-block > ul > li:nth-child(4)")
    ORDER_CALL_BUTTON = (By.CSS_SELECTOR, "a.order-call-btn")
    ORDER_CALL_FORM = (By.CSS_SELECTOR, ".form.submit-call-order")
    NAME_FIELD_OF_ORDER_CALL_FORM = (By.CSS_SELECTOR, "#call_black > div > div > div.modal-body > form > div > div > div:nth-child(1) > input")
    PHONE_FIELD_OF_ORDER_CALL_FORM = (By.CSS_SELECTOR, "#call_black > div > div > div.modal-body > form > div > div > div:nth-child(2) > input")
    SEND_BUTTON = (By.CSS_SELECTOR, "div.modal-body > form > div > button")
    REQUIRED_FIELD_RED_ERROR = (By.CSS_SELECTOR, "#phone-error")
    CLOSE_BUTTON_OF_ORDER_CALL_FORM = (By.CSS_SELECTOR, "#call_black > div > div > div.modal-header > button")
    DROPDOWN_MENU = (By.CSS_SELECTOR, ".dropdown")
    PHONE_NUMBERS_IN_DROPDOWN_MENU = (By.CSS_SELECTOR, ".dropdown li")
    SHOPPING_CART_ICON = (By.CSS_SELECTOR, ".top-menu__cart-info-orders-count-body")
    PRODUCT_IMG = (By.CSS_SELECTOR, ".products__item-thumb")
    TO_THE_BASKET_BUTTON = (By.CSS_SELECTOR, ".single-product__content button.single-product__order-button")
    SHOPPING_CART_WINDOW = (By.CSS_SELECTOR, ".cart__products")

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

    def hover_cursor(self, element_to_hover):
        ActionChains(self.browser).move_to_element(element_to_hover).perform()

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

    def click_on_delivery_and_payment_link_footer(self):
        link = self.browser.find_element(*self.LINK_ON_FOOTER_DELIVERY_AND_PAYMENT)
        link.click()

    def click_on_news_link_footer(self):
        link = self.browser.find_element(*self.LINK_ON_FOOTER_NEWS)
        link.click()

    def click_on_offer_link_footer(self):
        link = self.browser.find_element(*self.LINK_ON_FOOTER_OFFERTA)
        link.click()

    def note_the_address_and_go_to_google_maps_window(self, index):
        note_address = self.browser.find_element(*self.ADDRESS_OF_SHAURMAN)
        note_address_text = note_address.text
        note_address.click()
        self.browser.switch_to.window(self.browser.window_handles[index])
        return note_address_text

    def click_on_about_us_link_top_bar(self):
        link = self.browser.find_element(*self.LINK_ABOUT_US_TOP_BAR)
        link.click()

    def click_on_delivery_and_payment_link_top_bar(self):
        link = self.browser.find_element(*self.LINK_ON_TOP_BAR_DELIVERY_AND_PAYMENT)
        link.click()

    def click_on_news_link_top_bar(self):
        link = self.browser.find_element(*self.LINK_ON_TOP_BAR_NEWS)
        link.click()

    def click_on_request_the_call_button(self):
        link = self.browser.find_element(*self.ORDER_CALL_BUTTON)
        link.click()

    def verify_visibility_of_back_call_form(self):
        self._is_element_visible(*self.ORDER_CALL_FORM)

    def fill_optional_form(self):
        optional_form = self.browser.find_element(*self.NAME_FIELD_OF_ORDER_CALL_FORM)
        optional_form.send_keys("gafhjaejtaetj")

    def click_send_button(self):
        send_button = self.browser.find_element(*self.SEND_BUTTON)
        send_button.click()

    def verify_visibility_of_error_on_required_fields(self):
        self._is_element_visible(*self.REQUIRED_FIELD_RED_ERROR)

    def click_on_close_button_of_back_call_form(self):
        close_button = self.browser.find_element(*self.CLOSE_BUTTON_OF_ORDER_CALL_FORM)
        close_button.click()

    def verify_not_visibility_of_back_call_form(self):
        self._is_not_element_visible(*self.ORDER_CALL_FORM)

    def hover_cursor_over_the_drop_down_list(self):
        element_to_hover = self.browser.find_element(*self.DROPDOWN_MENU)
        self.hover_cursor(element_to_hover)

    def verify_visibility_of_drop_down_menu_with_telephone_numbers(self):
        self._is_element_visible(*self.PHONE_NUMBERS_IN_DROPDOWN_MENU)

    def click_on_shopping_cart_icon(self):
        shopping_cart_icon = self.browser.find_element(*self.SHOPPING_CART_ICON)
        shopping_cart_icon.click()

    def verify_displaying_shopping_cart_icon(self):
        self._is_element_visible(*self.SHOPPING_CART_ICON)

    def click_on_image_and_go_to_product_page(self, arg):
        self.browser.find_elements(*self.PRODUCT_IMG)[arg].click()

    def click_basket_button(self):
        basket_button = self.browser.find_element(*self.TO_THE_BASKET_BUTTON)
        basket_button.click()

    def shopping_cart_window_not_visible(self):
        self._is_not_element_visible(*self.SHOPPING_CART_WINDOW)

    def shopping_cart_window_is_visible(self):
        self._is_element_visible(*self.SHOPPING_CART_WINDOW)


