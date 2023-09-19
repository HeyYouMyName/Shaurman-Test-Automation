import time

from libraries.testrail import testrail
from pages.home_page import HomePage


class TestProductListPage:
    @testrail("PLP_001")
    def test_navigating_product_list_page(
            self,
            browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.click_on_sidebar_random_item()
        time.sleep(1)
