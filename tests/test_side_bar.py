from libraries.testrail import testrail
from pages.home_page import HomePage
from pages.facebook_page import FacebookPage
from pages.instagram_page import InstagramPage
from pages.product_list_page import ProductListPage
from pages.product_page import ProductPage
import pytest


class TestSideBar:
    NUMBER_OF_SIDEBAR_CATEGORIES = 17

    @testrail("SB_001")
    def test_the_presence_of_up_button(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.scroll_to_bottom()
        home_page.verify_presence_of_up_button()

    @testrail("SB_002")
    def test_the_work_of_up_button(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.scroll_to_bottom()
        home_page.click_up_button()
        home_page.verify_page_scrolled_to_top()

    @testrail("SB_003")
    @pytest.mark.parametrize("sidebar_category", range(NUMBER_OF_SIDEBAR_CATEGORIES))
    def test_following_the_category_links(
        self,
        browser,
        sidebar_category,
    ):
        home_page = HomePage(browser)
        home_page.open()
        name_on_side_bar = home_page.get_text_of_sidebar_category(sidebar_category).lower()
        home_page.click_on_sidebar_category(sidebar_category)
        product_list_page = ProductListPage(browser)
        name_on_product_list_page = product_list_page.get_hold_of_all_products_name().text.lower()
        home_page.check_that_you_are_on_right_product_list_page(name_on_product_list_page, name_on_side_bar)
    #     no page named акції та знижки

    @testrail("SB_005")
    def test_following_the_facebook_link(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_facebook_button()
        facebook_page = FacebookPage(browser)
        facebook_page.check_facebook_text_in_url()

    @testrail("SB_006")
    def test_following_the_instagram_link(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_instagram_button()
        instagram_page = InstagramPage(browser)
        instagram_page.check_instagram_text_in_url()

    @testrail("SB_007")
    def test_presence_of_logo(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.verify_presence_of_logo()

    @testrail("SB_008")
    @pytest.mark.parametrize("sidebar_category, product", [(s, p) for s in range(3) for p in range(2)])
    def verify_the_link_on_shaurman_logo(
        self,
        browser,
        sidebar_category,
        product,
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(sidebar_category)
        product_list_page = ProductListPage(browser)
        product_list_page.click_on_the_logo()
        home_page.check_presence_on_the_home_page()
        home_page.click_on_sidebar_category(sidebar_category)
        product_list_page = ProductListPage(browser)
        product_list_page.click_on_product_on_product_list_page(product)
        product_page = ProductPage(browser)
        product_page.click_on_the_logo()
        home_page.check_presence_on_the_home_page()
