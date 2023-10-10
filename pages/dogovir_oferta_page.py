from pages.base_page import BasePage


class DogovirOfertaPage(BasePage):

    def check_publichnyj_dogovor_oferta_text_in_url(self) -> None:
        current_url = self.browser.current_url
        assert "publichnyj-dogovor-oferta" in current_url
