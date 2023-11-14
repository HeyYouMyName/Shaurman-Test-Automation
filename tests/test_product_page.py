from libraries.testrail import testrail
from pages.home_page import HomePage
from pages.product_list_page import ProductListPage
from pages.product_page import ProductPage


class TestProductListPage:
    @testrail("PP_001")
    def test_navigating_to_product_page(
        self,
        browser,
        product_index=1
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(2)
        product_list_page = ProductListPage(browser)
        product_list_page.click_on_image_and_go_to_product_page(product_index)

    @testrail("PP_002")
    def test_add_shopping_cart_required_blank(
        self,
        browser,
        product_index=1
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(4)
        product_list_page = ProductListPage(browser)
        product_list_page.click_on_image_and_go_to_product_page(product_index)
        product_page = ProductPage(browser)
        product_page.click_on_basket_button()
        product_page.check_cake_nessesary_text_is_displayed()

    @testrail("PP_003")
    def test_add_shopping_cart_required_filled(
        self,
        browser,
        product_index=1
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(5)
        product_list_page = ProductListPage(browser)
        product_list_page.click_on_image_and_go_to_product_page(product_index)
        product_page = ProductPage(browser)
        product_page.choose_main_ingredient(0)
        product_page.scroll_to_bottom()
        product_page.click_basket_button2()
        product_page.check_number_of_items_in_the_basket(1)

    @testrail("PP_004")
    def test_add_additional_ingredient(
        self,
        browser,
        product_index=1
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(5)
        product_list_page = ProductListPage(browser)
        product_list_page.click_on_image_and_go_to_product_page(product_index)
        product_page = ProductPage(browser)
        product_page.choose_main_ingredient(0)
        product_page.scroll_to_bottom()
        product_page.add_additional_ingredient(7)

    @testrail("PP_005")
    def test_remove_additional_ingredient(
        self,
        browser,
        product_index=1
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(5)
        product_list_page = ProductListPage(browser)
        product_list_page.click_on_image_and_go_to_product_page(product_index)
        product_page = ProductPage(browser)
        product_page.choose_main_ingredient(0)
        product_page.scroll_to_bottom()
        price_before = product_page.add_additional_ingredient(7)
        product_page.delete_additional_ingredient(7, price_before)

    @testrail("PP_006")
    def test_zoomed_image(
        self,
        browser,
        product_index=1
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(2)
        product_list_page = ProductListPage(browser)
        product_list_page.click_on_image_and_go_to_product_page(product_index)
        product_page = ProductPage(browser)
        product_page.click_product_image()

    @testrail("PP_007")
    def test_zoomed_image_close(
        self,
        browser,
        product_index=1
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(2)
        product_list_page = ProductListPage(browser)
        product_list_page.click_on_image_and_go_to_product_page(product_index)
        product_page = ProductPage(browser)
        product_page.click_product_image()
        product_page.close_product_image()

    @testrail("PP_008")
    def test_product_name_equals(
        self,
        browser,
        product_index=1
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(2)
        product_list_page = ProductListPage(browser)
        product_list_page.click_on_image_and_go_to_product_page(product_index)
        product_page = ProductPage(browser)
        product_page.check_product_name()
