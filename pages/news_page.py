from pages.base_page import BasePage


class NewsPage(BasePage):

    def check_blog_text_in_url(self) -> None:
        current_url = self.browser.current_url
        assert "/blog" in current_url
