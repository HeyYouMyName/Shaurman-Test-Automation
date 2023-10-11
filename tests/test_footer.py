from libraries.testrail import testrail
from pages.home_page import HomePage
from pages.google_maps_page import GoogleMapsPage
from pages.delivery_and_payment import DeliveryAndPaymentPage
from pages.news_page import NewsPage
from pages.dogovir_oferta_page import DogovirOfertaPage


class TestFooter:
    @testrail("F_001")
    def test_delivery_and_payment_link_in_footer(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.scroll_to_bottom()
        home_page.click_on_delivery_and_payment_link_footer()
        delivery_and_payment = DeliveryAndPaymentPage(browser)
        delivery_and_payment.check_delivery_text_in_url()

    @testrail("F_002")
    def test_news_link_in_footer(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.scroll_to_bottom()
        home_page.click_on_news_link_footer()
        news_page = NewsPage(browser)
        news_page.check_blog_text_in_url()

    @testrail("F_003")
    def test_offer_link_in_footer(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.scroll_to_bottom()
        home_page.click_on_offer_link_footer()
        dogovir_oferta_page = DogovirOfertaPage(browser)
        dogovir_oferta_page.check_publichnyj_dogovor_oferta_text_in_url()

    @testrail("F_004")
    def test_that_map_opens_correct_address(
        self,
        browser
    ):
        home_page = HomePage(browser)
        home_page.open()
        home_page.scroll_to_bottom()
        note_address_text = home_page.note_the_address_and_go_to_google_maps_window(1)
        google_maps = GoogleMapsPage(browser)
        google_maps.check_address_on_maps_page_equals_to_shaurman(note_address_text)
