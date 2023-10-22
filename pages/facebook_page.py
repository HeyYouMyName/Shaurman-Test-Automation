from pages.base_page import BasePage


class FacebookPage(BasePage):

    def check_facebook_text_in_url(self) -> None:
        current_url = self.browser.current_url
        assert "https://www.facebook.com/shaurman" in current_url