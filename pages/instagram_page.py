from pages.base_page import BasePage


class InstagramPage(BasePage):

    def check_instagram_text_in_url(self) -> None:
        current_url = self.browser.current_url
        assert "https://www.instagram.com/shaurman1/" in current_url
