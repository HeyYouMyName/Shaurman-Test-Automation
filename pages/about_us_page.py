from pages.base_page import BasePage


class AboutUs(BasePage):

    def check_about_us_text_in_url(self) -> None:
        current_url = self.browser.current_url
        assert "/about_us" in current_url

