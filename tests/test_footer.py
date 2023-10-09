
from libraries.testrail import testrail
from pages.home_page import HomePage
from pages.footer import Footer


class TestProductListPage:
    @testrail("F_001")
    def test_delivery_and_payment_link_in_footer(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.scroll_to_bottom()
        footer = Footer(browser)
        footer.click_on_delivery_and_payment_link(1)

    @testrail("F_002")
    def test_news_link_in_footer(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.scroll_to_bottom()
        footer = Footer(browser)
        footer.click_on_news_link(2)

    @testrail("F_003")
    def test_offer_link_in_footer(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.scroll_to_bottom()
        footer = Footer(browser)
        footer.click_on_offer_link(3)

    @testrail("F_004")
    def test_that_map_opens_correct_address(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.scroll_to_bottom()
        footer = Footer(browser)
        footer.verifying_that_map_opens_the_correct_address(1)






