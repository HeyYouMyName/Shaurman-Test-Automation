from libraries.testrail import testrail
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.product_list_page import ProductListPage
import time


class TestFooter:
    @testrail("SC_001")
    def test_shopping_cart_icon_is_displayed_on_the_home_page(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.verify_displaying_shopping_cart_icon()

    @testrail("SC_002")
    def test_the_shopping_cart_button_when_no_products_are_added_to_the_shopping_cart(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_shopping_cart_icon()
        home_page.shopping_cart_window_is_not_visible()

    @testrail("SC_003")
    def test_adding_one_item_to_the_cart(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(16)
        product_list_page = ProductListPage(browser)
        product_list_page.click_on_product_on_product_page(0)
        product_page = ProductPage(browser)
        product_page.click_on_basket_button()
        product_page.wait_till_text_present_in_shopping_cart_icon("1")
        product_page.verify_presence_of_text_and_number_of_items_in_shopping_cart_icon(1)
        product_page.click_on_shopping_cart_icon()
        product_page.shopping_cart_window_is_visible()
        product_page.verify_visibility_of_products_in_shopping_cart()

    @testrail("SC_004")
    def test_closing_shopping_cart(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(16)
        product_list_page = ProductListPage(browser)
        product_list_page.click_on_order_button(0)
        product_list_page.wait_till_text_present_in_shopping_cart_icon("1")
        product_list_page.click_on_shopping_cart_icon()
        product_list_page.shopping_cart_window_is_visible()
        product_list_page.click_on_shopping_cart_icon()
        product_list_page.shopping_cart_window_is_not_visible()

    @testrail("SC_005")
    def test_click_on_the_product_name_to_view_the_ingredient_list(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(3)
        product_list_page = ProductListPage(browser)
        product_list_page.click_on_order_button(0)
        product_page = ProductPage(browser)
        product_page.choose_main_ingredient(0)
        product_page.click_basket_button2()
        product_page.click_on_shopping_cart_icon()
        product_page.click_on_product_name_on_product_page()
        product_page.verify_visibility_of_products_in_shopping_cart()

    @testrail("SC_006")
    def test_removing_single_item_from_shopping_cart(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(16)
        product_list_page = ProductListPage(browser)
        product_list_page.click_on_order_button(0)
        product_list_page.wait_till_text_present_in_shopping_cart_icon("1")
        product_list_page.click_on_shopping_cart_icon()
        product_list_page.click_on_delete_button_in_shopping_cart_menu(0)
        product_list_page.wait_till_text_present_in_shopping_cart_icon("0")
        product_list_page.shopping_cart_window_is_not_visible()
        product_list_page.verify_presence_of_text_and_number_of_items_in_shopping_cart_icon(0)

    @testrail("SC_007")
    def test_removing_single_item_from_many_in_the_shopping_cart(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(16)
        product_list_page = ProductListPage(browser)
        product_list_page.click_on_order_button(0)
        product_list_page.click_on_order_button(1)
        product_list_page.click_on_order_button(2)
        product_list_page.click_on_shopping_cart_icon()
        product_list_page.wait_for_delete_button_to_appear_in_shopping_cart_menu()
        product = product_list_page.product_to_be_deleted_from_shopping_cart_menu(0)
        product_list_page.click_on_delete_button_in_shopping_cart_menu(0)
        product_list_page.check_that_product_deleted_from_shopping_cart_menu(product)
        time.sleep(1)
