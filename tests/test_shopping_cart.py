from libraries.testrail import testrail
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.product_list_page import ProductListPage


class TestShoppingCart:
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
        product_list_page.click_on_product_on_product_list_page(0)
        product_page = ProductPage(browser)
        product_page.click_on_basket_button()
        product_page.wait_till_text_present_in_shopping_cart_icon("1")
        product_page.verify_presence_of_number_of_items_in_shopping_cart_icon(1)
        product_page.verify_presence_of_text_in_shopping_cart_icon()
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
        product_list_page.verify_presence_of_number_of_items_in_shopping_cart_icon(0)

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

    @testrail("SC_008")
    def test_adding_more_than_4_items_to_the_shopping_cart(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(15)
        product_list_page = ProductListPage(browser)
        product_list_page.click_on_order_button(0)
        product_list_page.click_on_order_button(1)
        product_list_page.click_on_order_button(2)
        product_list_page.click_on_order_button(3)
        product_list_page.click_on_order_button(4)
        product_list_page.click_on_shopping_cart_icon()
        product_list_page.check_that_cart_carousel_is_visible()

    @testrail("SC_009")
    def test_image_name_and_price_of_the_product_item_in_the_shopping_cart(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(16)
        product_list_page = ProductListPage(browser)
        product_list_page.click_on_product_on_product_list_page(0)
        product_page = ProductPage(browser)
        product_page.click_on_basket_button()
        product_list_page.wait_till_text_present_in_shopping_cart_icon("1")
        order_quantity = product_page.get_order_quantity()
        product_page.click_on_shopping_cart_icon()
        product_page.check_that_price_of_a_product_is_visible_in_the_cart()
        product_page.check_that_name_of_a_product_is_visible_in_the_cart()
        product_page.check_that_img_of_a_product_is_visible_in_the_cart()
        product_page.check_that_price_on_product_page_equals_to_the_price_in_the_cart()
        product_page.check_that_name_on_product_page_equals_to_the_name_in_the_cart()
        product_page.check_that_img_on_product_page_equals_to_the_img_in_the_cart()
        product_page.check_that_order_quantity_is_correct(order_quantity)

    @testrail("SC_010")
    def test_pay_by_card(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(15)
        product_list_page = ProductListPage(browser)
        product_list_page.click_on_order_button(0)
        product_list_page.wait_till_text_present_in_shopping_cart_icon("1")
        product_list_page.click_on_shopping_cart_icon()
        product_list_page.click_on_pay_by_card_button()
        product_list_page.verify_fast_order_form_is_visible()

    @testrail("SC_011")
    def test_pay_to_courier(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(15)
        product_list_page = ProductListPage(browser)
        product_list_page.click_on_order_button(0)
        product_list_page.wait_till_text_present_in_shopping_cart_icon("1")
        product_list_page.click_on_shopping_cart_icon()
        product_list_page.click_on_pay_to_courier_button()
        product_list_page.verify_fast_order_form_is_visible()

    @testrail("SC_012")
    def test_increasing_the_quantity_of_the_product_in_the_shopping_cart_page(
        self,
        browser,
        position_in_product_list=0
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(15)
        product_list_page = ProductListPage(browser)
        product_list_page.click_on_order_button(position_in_product_list)
        price_product = product_list_page.get_the_price_on_the_product_list_page(position_in_product_list)
        product_list_page.wait_till_text_present_in_shopping_cart_icon("1")
        product_list_page.click_on_shopping_cart_icon()
        product_list_page.click_on_plus_button_in_cart()
        order_quantity = product_list_page.get_order_quantity_in_the_shopping_cart()
        product_list_page.check_that_order_quantity_is_correct(order_quantity)
        product_list_page.check_that_double_price_on_product_page_equals_to_the_increased_price_in_the_cart(price_product, 2)

    @testrail("SC_013")
    def test_updating_the_quantity_of_the_product_in_the_shopping_cart_to_a_negative_or_zero_or_a_non_numerical_value(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(15)
        product_list_page = ProductListPage(browser)
        product_list_page.click_on_order_button(0)
        product_list_page.wait_till_text_present_in_shopping_cart_icon("1")
        product_list_page.click_on_shopping_cart_icon()
        price_before_clicking_minus_button = product_list_page.get_the_price_in_the_cart()
        product_list_page.click_on_minus_button_in_cart()
        price_after_clicking_minus_button = product_list_page.get_the_price_in_the_cart()
        product_list_page.check_prices_are_equal(price_before_clicking_minus_button, price_after_clicking_minus_button)

    @testrail("SC_014")
    def test_the_shopping_cart_button_when_there_are_products_added_to_the_shopping_cart(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(16)
        product_list_page = ProductListPage(browser)
        product_list_page.click_on_product_on_product_list_page(0)
        product_page = ProductPage(browser)
        product_page.click_on_basket_button()
        product_page.wait_till_text_present_in_shopping_cart_icon("1")
        product_page.click_on_shopping_cart_icon()
        product_page.shopping_cart_window_is_visible()
#         the 15 test case is the same as 13
