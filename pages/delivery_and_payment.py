from pages.base_page import BasePage


class DeliveryAndPaymentPage(BasePage):

    def check_delivery_text_in_url(self) -> None:
        current_url = self.browser.current_url
        assert "delivery" in current_url
