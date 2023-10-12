from libraries.testrail import testrail
from pages.home_page import HomePage
from pages.delivery_and_payment import DeliveryAndPaymentPage
from pages.news_page import NewsPage
from pages.about_us_page import AboutUs


class TestTopBarMenu:
    @testrail("TBM_001")
    def test_about_us_link_in_top_bar(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_about_us_link_top_bar()
        about_us = AboutUs(browser)
        about_us.check_about_us_text_in_url()

    @testrail("TBM_002")
    def test_delivery_and_payment_link_in_top_bar(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_delivery_and_payment_link_top_bar()
        delivery_and_payment = DeliveryAndPaymentPage(browser)
        delivery_and_payment.check_delivery_text_in_url()

    @testrail("TBM_003")
    def test_news_link_in_top_bar(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_news_link_top_bar()
        news_page = NewsPage(browser)
        news_page.check_blog_text_in_url()

    @testrail("TBM_004")
    def test_order_call_in_top_bar(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_request_the_call_button()
        home_page.verify_visibility_of_back_call_form()

    @testrail("TBM_005")
    def test_order_call_with_empty_required_fields(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_request_the_call_button()
        home_page.fill_optional_form()
        home_page.click_send_button()
        home_page.verify_visibility_of_error_on_required_fields()

    @testrail("TBM_006")
    def test_order_call_with_all_empty_fields(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_request_the_call_button()
        home_page.click_send_button()
        home_page.verify_visibility_of_error_on_required_fields()

    @testrail("TBM_007")
    def test_the_close_button_of_order_call(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_request_the_call_button()
        home_page.click_on_close_button_of_back_call_form()
        home_page.verify_not_visibility_of_back_call_form()

    @testrail("TBM_008")
    def test_dropdown_menu_top_bar(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.hover_cursor_over_the_drop_down_list()
        home_page.verify_visibility_of_drop_down_menu_with_telephone_numbers()

    @testrail("TBM_009")
    def test_cart_button_when_products_are_not_added_to_shopping_cart(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_shopping_cart_icon()
        home_page.shopping_cart_window_not_visible()

    @testrail("TBM_010")
    def test_cart_button_when_products_are_added_to_shopping_cart(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(16)
        home_page.click_on_image_and_go_to_product_page(1)
        home_page.click_basket_button()
        home_page.click_on_shopping_cart_icon()
        home_page.shopping_cart_window_is_visible()

    @testrail("TBM_011")
    def test_displaying_shopping_cart_icon(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.verify_displaying_shopping_cart_icon()
