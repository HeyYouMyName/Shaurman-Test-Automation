import pytest

from pages.home_page import HomePage
from libraries.testrail import testrail


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
