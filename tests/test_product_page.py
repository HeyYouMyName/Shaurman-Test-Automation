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

