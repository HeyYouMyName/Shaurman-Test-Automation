# @testrail("SB_00000001")
# @pytest.mark.parametrize("sidebar_category", range(NUMBER_OF_SIDEBAR_CATEGORIES))
# def test_test(
#     self,
#     browser,
#     sidebar_category,
# ):
#     home_page = HomePage(browser)
#     home_page.open()
#     home_page.click_on_sidebar_category(sidebar_category)
#     product_list_page = ProductListPage(browser)
#     self.new.append(product_list_page.return_click_on_first_product_on_product_page())
#     print(self.new)
MY_LIST = [2, 5, 7, 7, 7, 15, 4, 4, 5, 4, 2, 5, 5, 17, 14]
FEAST_FOR_DECORATOR = [(s, p) for s in range(2) for p in range(MY_LIST[s])]
print(FEAST_FOR_DECORATOR)
