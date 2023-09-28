from libraries.testrail import testrail

from pages.home_page import HomePage
from pages.product_list_page import ProductListPage
from pages.product_page import ProductPage


class TestProductListPage:
    @testrail("PLP_001")
    def test_navigating_product_list_page(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(2)

    @testrail("PLP_002")
    def test_change_order_buttons_check(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(0)
        product_list_page = ProductListPage(browser)
        product_list_page.check_change_button_present()
        product_list_page.check_order_button_present()

    @testrail("PLP_003")
    def test_title_weight_price_ingredients_check(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(9)
        product_list_page = ProductListPage(browser)
        product_list_page.check_product_title_weight_price_ingredients_present()

    @testrail("PLP_004")
    def test_change_button_click(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(9)
        product_list_page = ProductListPage(browser)
        product_list_page.click_on_change_button(3)

    @testrail("PLP_005")
    def test_order_button_not_required(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(9)
        product_list_page = ProductListPage(browser)
        product_list_page.click_on_order_button(1)

    @testrail("PLP_006")
    def test_order_button_required(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(3)
        product_list_page = ProductListPage(browser)
        product_list_page.click_on_order_button(3)

    @testrail("PLP_007")
    def test_match_prices(
        self,
        browser,
        product_index=1
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(1)
        product_list_page = ProductListPage(browser)
        val1 = product_list_page.get_hold_of_price(product_index)
        product_list_page.click_image_way_to_product_page(product_index)
        product_page = ProductPage(browser)
        val2 = product_page.get_price_on_product()
        product_list_page.check_prices_are_equal(val1, val2)
