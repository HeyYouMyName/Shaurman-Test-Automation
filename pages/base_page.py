from selenium.common import TimeoutException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time


class BasePage:
    URL = r"https://shaurman.com.ua/"

    # Locators
    SIDEBAR_BLOCK = (By.CSS_SELECTOR, "div.sidebar")
    TOP_BAR_BLOCK = (By.CSS_SELECTOR, "div.top-menu")
    FOOTER_CONTAINER = (By.CSS_SELECTOR, "div.footer__container")
    MAIN_CONTENT_BLOCK = (By.CSS_SELECTOR, "#content.main")
    SIDEBAR_ITEMS = (By.CSS_SELECTOR, "div.sidebar > ul:nth-child(2) > li")
    SIDEBAR_ITEMS_TEXT = (By.CSS_SELECTOR, "div.sidebar > ul:nth-child(2)  > li > a >  span")
    LINK_ON_FOOTER_DELIVERY_AND_PAYMENT = (By.CSS_SELECTOR, "div.footer__nav > ul > li:nth-child(2) > a")
    LINK_ON_FOOTER_NEWS = (By.CSS_SELECTOR, "div.footer__nav > ul > li:nth-child(3) > a")
    LINK_ON_FOOTER_OFFERTA = (By.CSS_SELECTOR, "div.footer__nav > ul > li:nth-child(4) > a")
    ADDRESS_OF_SHAURMAN = (By.CSS_SELECTOR, "div.footer__address a")
    LINK_ABOUT_US_TOP_BAR = (By.CSS_SELECTOR, "div.top-menu__nav-block > ul > li:nth-child(2)")
    LINK_ON_TOP_BAR_DELIVERY_AND_PAYMENT = (By.CSS_SELECTOR, "div.top-menu__nav-block > ul > li:nth-child(3)")
    LINK_ON_TOP_BAR_NEWS = (By.CSS_SELECTOR, "div.top-menu__nav-block > ul > li:nth-child(4)")
    ORDER_CALL_BUTTON = (By.CSS_SELECTOR, "a.order-call-btn")
    ORDER_CALL_FORM = (By.CSS_SELECTOR, ".form.submit-call-order .modal-body__content.modal-body__content--padding-big")
    NAME_FIELD_OF_ORDER_CALL_FORM = (By.CSS_SELECTOR, "#call_black > div > div > div.modal-body > form > div > div > div:nth-child(1) > input")
    PHONE_FIELD_OF_ORDER_CALL_FORM = (By.CSS_SELECTOR, "#call_black > div > div > div.modal-body > form > div > div > div:nth-child(2) > input")
    SEND_BUTTON = (By.CSS_SELECTOR, "div.modal-body > form > div > button")
    REQUIRED_FIELD_RED_ERROR = (By.CSS_SELECTOR, ".form-control.error")
    CLOSE_BUTTON_OF_ORDER_CALL_FORM = (By.CSS_SELECTOR, "#call_black > div > div > div.modal-header > button")
    DROPDOWN_MENU = (By.CSS_SELECTOR, ".dropdown")
    PHONE_NUMBERS_IN_DROPDOWN_MENU = (By.CSS_SELECTOR, ".dropdown li")
    SHOPPING_CART_ICON = (By.CSS_SELECTOR, ".top-menu__cart-info-orders-count-body")
    PRODUCT_IMG = (By.CSS_SELECTOR, ".products__item-thumb")
    TO_THE_BASKET_BUTTON = (By.CSS_SELECTOR, ".single-product__content button.single-product__order-button")
    SHOPPING_CART_WINDOW = (By.CSS_SELECTOR, ".cart__products")
    UP_BUTTON = (By.CSS_SELECTOR, ".sidebar__button-up")
    SOCIAL_BUTTONS = (By.CSS_SELECTOR, ".sidebar__socials li")
    SHAURMAN_LOGO = (By.CSS_SELECTOR, ".sidebar-nav__brand")

    def __init__(
        self,
        browser: webdriver
    ):
        self.browser = browser

    @staticmethod
    def retry_until_result(desired_result, max_retries, interval_seconds):
        def decorator(func):
            def wrapper(*args, **kwargs):
                for _ in range(max_retries):
                    result = func(*args, **kwargs)
                    if result == desired_result:
                        return result
                    time.sleep(interval_seconds)
                raise Exception("Desired result not achieved after {} retries".format(max_retries))
            return wrapper
        return decorator

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

    def _is_element_invisible(
        self,
        locator: str,
        selector: str,
        timeout: int = 1
    ) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.invisibility_of_element_located((locator, selector))
            )
        except TimeoutException:
            return False
        return True

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

    def click_on_sidebar_category(self, index):
        side_bar_menu = self.browser.find_elements(*self.SIDEBAR_ITEMS)
        side_bar_menu[index].click()

    def get_text_of_sidebar_category(self, index):
        side_bar_menu_text = self.browser.find_elements(*self.SIDEBAR_ITEMS_TEXT)
        return side_bar_menu_text[index].text

    @staticmethod
    def check_that_you_are_on_right_product_list_page(name1, name2):
        assert name1 == name2

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
        assert self._is_element_visible(*self.ORDER_CALL_FORM)

    def fill_optional_form(self):
        optional_form = self.browser.find_element(*self.NAME_FIELD_OF_ORDER_CALL_FORM)
        optional_form.send_keys("gafhjaejtaetj")

    def click_send_button(self):
        send_button = self.browser.find_element(*self.SEND_BUTTON)
        send_button.click()

    def verify_visibility_of_error_on_required_fields(self):
        assert self._is_element_visible(*self.REQUIRED_FIELD_RED_ERROR)

    def click_on_close_button_of_back_call_form(self):
        close_button = self.browser.find_element(*self.CLOSE_BUTTON_OF_ORDER_CALL_FORM)
        close_button.click()

    def verify_not_visibility_of_back_call_form(self):
        assert self._is_element_invisible(*self.ORDER_CALL_FORM)

    def hover_cursor_over_the_drop_down_list(self):
        element_to_hover = self.browser.find_element(*self.DROPDOWN_MENU)
        self.hover_cursor(element_to_hover)

    def verify_visibility_of_drop_down_menu_with_telephone_numbers(self):
        assert self._is_element_visible(*self.PHONE_NUMBERS_IN_DROPDOWN_MENU)

    def click_on_shopping_cart_icon(self):
        shopping_cart_icon = self.browser.find_element(*self.SHOPPING_CART_ICON)
        shopping_cart_icon.click()

    def verify_displaying_shopping_cart_icon(self):
        assert self._is_element_visible(*self.SHOPPING_CART_ICON)

    def click_on_image_and_go_to_product_page(self, arg):
        self.browser.find_elements(*self.PRODUCT_IMG)[arg].click()

    def click_basket_button(self):
        basket_button = self.browser.find_element(*self.TO_THE_BASKET_BUTTON)
        basket_button.click()

    def shopping_cart_window_not_visible(self):
        assert self._is_not_element_visible(*self.SHOPPING_CART_WINDOW)

    def shopping_cart_window_is_visible(self):
        assert self._is_element_visible(*self.SHOPPING_CART_WINDOW)

    def verify_presence_of_up_button(self):
        assert self._is_element_visible(*self.UP_BUTTON)

    def click_up_button(self):
        button = self.browser.find_element(*self.UP_BUTTON)
        button.click()

    def click_on_facebook_button(self):
        buttons = self.browser.find_elements(*self.SOCIAL_BUTTONS)
        buttons[1].click()
        self.browser.switch_to.window(self.browser.window_handles[1])

    def click_on_instagram_button(self):
        buttons = self.browser.find_elements(*self.SOCIAL_BUTTONS)
        buttons[0].click()
        self.browser.switch_to.window(self.browser.window_handles[1])

    def verify_presence_of_logo(self):
        assert self._is_element_visible(*self.SHAURMAN_LOGO)

    @retry_until_result(desired_result=0, max_retries=5, interval_seconds=1)
    def get_hold_of_top_top_position(self):
        scroll_position = self.browser.execute_script("return window.scrollY;")
        return scroll_position

    @staticmethod
    def verify_position_on_the_top_of_the_page(func):
        assert func == 0

    def click_on_product_on_product_page(self, index):
        list_of_products_imgs = self.browser.find_elements(*self.PRODUCT_IMG)
        list_of_products_imgs[index].click()

    def click_on_the_logo(self):
        logo = self.browser.find_element(*self.SHAURMAN_LOGO)
        logo.click()
