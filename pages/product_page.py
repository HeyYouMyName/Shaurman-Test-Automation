from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    # Locators
    PRICE_ON_PRODUCT_PAGE = (By.CSS_SELECTOR, "div.single-product__content > div.single-product__order > p > span")
    CAKE_TEXT_WARNING_MESSAGE = (By.CSS_SELECTOR, "div.text-danger")
    TO_THE_BASKET_BUTTON = (By.CSS_SELECTOR, ".single-product__content button.single-product__order-button")
    TYPE_OF_CAKES = (By.CSS_SELECTOR, "div.product-sauces__sauce-image")
    TO_THE_BASKET_BUTTON2 = (By.CSS_SELECTOR, ".single-product__lets-try .single-product__order-button")
    NUMBER_OF_PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".top-menu__cart-info-orders-count-value")
    LIST_OF_ADDITIONAL_PRODUCT_INGRIDIENTS = (By.CSS_SELECTOR, ".single-product__attributes__right .product-ingridients li")
    PRICE_LOW = (By.CSS_SELECTOR, ".single-product__lets-try .single-product__price-value")
    LIST_OF_ADDITIONAL_PRODUCT_INGRIDIENTS_ADDED_TO_MAIN_PRODUCT = (By.CSS_SELECTOR, ".product-ingridients.product-ingridients--checked li")
    PRODUCT_IMAGE_PRODUCT_PAGE = (By.CSS_SELECTOR, ".single-product__image .thumbnails")
    PRODUCT_IMAGE_PRODUCT_PAGE_CLOSE_BUTTON = (By.CSS_SELECTOR, "button.mfp-close")
    PRODUCT_NAME = (By.CSS_SELECTOR, "p.single-product__title")
    PRODUCT_NAME_ZOOMED = (By.CSS_SELECTOR, "div.mfp-title")
    ADDITIONAL_PRODUCT_INGRIDIENT_PRICE = (By.CSS_SELECTOR, ".single-product__attributes__right ul.product-ingridients li .product-ingridients__ingridient-proportions")


    def check_number_of_items_in_the_basket(self, arg):
        assert self._is_element_clickable(*self.NUMBER_OF_PRODUCTS_IN_BASKET)
        number = self.browser.find_element(*self.NUMBER_OF_PRODUCTS_IN_BASKET).text
        assert int(number) == arg, "not added to basket"

    def get_price_on_product(self):
        price_product = self.browser.find_element(*self.PRICE_ON_PRODUCT_PAGE).text
        return price_product

    def click_basket_button(self):
        basket_button = self.browser.find_element(*self.TO_THE_BASKET_BUTTON)
        basket_button.click()

    def click_basket_button2(self):
        basket_button = self.browser.find_element(*self.TO_THE_BASKET_BUTTON2)
        basket_button.click()

    def click_on_type_of_cake(self, index):
        types_of_cake = self.browser.find_elements(*self.TYPE_OF_CAKES)
        assert self._is_element_clickable(*self.TYPE_OF_CAKES)
        types_of_cake[index].click()

    def check_cake_nessesary_text_is_displayed(self) -> None:
        assert self._is_element_visible(*self.CAKE_TEXT_WARNING_MESSAGE)

    def add_additional_ingredient(self, index):
        list_of_additional_ingredients = self.browser.find_elements(*self.LIST_OF_ADDITIONAL_PRODUCT_INGRIDIENTS)
        price_before = int(self.browser.find_element(*self.PRICE_LOW).text.split()[0])
        price_additional = int(self.browser.find_elements(*self.ADDITIONAL_PRODUCT_INGRIDIENT_PRICE)[index].text.split()[2][1::])
        list_of_additional_ingredients[index].click()
        price_after = int(self.browser.find_element(*self.PRICE_LOW).text.split()[0])
        assert price_after - price_before == price_additional
        return price_before

    def delete_additional_ingredient(self, index, price_before):
        list_of_additional_ingredients_added = self.browser.find_elements(*self.LIST_OF_ADDITIONAL_PRODUCT_INGRIDIENTS_ADDED_TO_MAIN_PRODUCT)
        list_of_additional_ingredients_added[index].click()
        price_after = int(self.browser.find_element(*self.PRICE_LOW).text.split()[0])
        assert price_before == price_after



    def click_product_image(self):
        product_image = self.browser.find_element(*self.PRODUCT_IMAGE_PRODUCT_PAGE)
        product_image.click()

    def close_product_image(self):
        close_button = self.browser.find_element(*self.PRODUCT_IMAGE_PRODUCT_PAGE_CLOSE_BUTTON)
        close_button.click()

    def check_product_name(self):
        product_name = self.browser.find_element(*self.PRODUCT_NAME).text
        self.click_product_image()
        product_name_zoomed = self.browser.find_element(*self.PRODUCT_NAME_ZOOMED).text
        assert product_name == product_name_zoomed
