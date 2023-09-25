import time

from libraries.testrail import testrail
from pages.home_page import HomePage
from pages.product_list_page import ProductListPage


class TestProductListPage:
    @testrail("PLP_001")
    def test_navigating_product_list_page(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(2)
        time.sleep(1)

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

        time.sleep(1)

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

        time.sleep(1)

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

        time.sleep(2)

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

        time.sleep(2)

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

        time.sleep(2)

    @testrail("PLP_007")
    def test_match_prices(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(9)
        product_list_page = ProductListPage(browser)
        product_list_page.check_price_equal(1)
        time.sleep(2)
