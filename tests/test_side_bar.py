from libraries.testrail import testrail
from pages.home_page import HomePage
from pages.facebook_page import FacebookPage
from pages.instagram_page import InstagramPage
from pages.product_list_page import ProductListPage
from pages.product_page import ProductPage
import pytest


class TestSideBar:
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
        home_page.verify_the_work_of_up_button()

    @testrail("SB_003")
    @pytest.mark.parametrize("sidebar_category", [sidebar_category for sidebar_category in range(0, 18)])
    def test_following_the_category_links(
        self,
        browser,
        sidebar_category
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(sidebar_category)

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
    @pytest.mark.parametrize("sidebar_category", [sidebar_category for sidebar_category in range(0, 18)])
    def test_following_the_category_links(
        self,
        browser,
        sidebar_category
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_category(sidebar_category)
        product_list_page = ProductListPage(browser)
        product_list_page.click_on_the_logo()
        home_page.click_on_sidebar_category(sidebar_category)
        product_list_page = ProductListPage(browser)
        product_list_page.click_on_first_product_on_product_page()
        product_page = ProductPage(browser)
        product_page.click_on_the_logo()
