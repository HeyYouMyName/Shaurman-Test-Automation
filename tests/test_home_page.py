import pytest

from libraries.testrail import testrail
from pages.home_page import HomePage


@pytest.mark.home_page
class TestHomePage:
    @testrail("HP_001")
    def test_displaying_sidebar(
            self,
            browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.check_sidebar_present()

    @testrail("HP_002")
    def test_displaying_topbar(
            self,
            browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.check_tob_bar_present()

    @testrail("HP_003")
    def test_slider_present(
            self,
            browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.check_slider_present()

    @testrail("HP_003")
    def test_slider_present(
            self,
            browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.check_slider_present()

    @testrail("HP_004")
    def test_main_content_present(
            self,
            browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.check_main_content_block_present()

    @testrail("HP_005")
    def test_footer_present(
            self,
            browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.scroll_to_bottom()
        home_page.check_footer_container_present()
