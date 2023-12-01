import pytest
import allure

from base.base_test import BaseTest
from config.locators_pytest_param import ParametrizationData


@allure.feature("Women page functionality")
class TestWomenCatalogFeatures(BaseTest):
    PRICE = "price"

    @pytest.fixture()
    def _setup_page(self, browser):
        self.women_page.open()
        self.women_page.is_opened(self.women_page.PAGE_TITLE)
        self.women_page.click_on_category(self.women_page.WOMEN_TOPS)

    @allure.title("Women category page is opened")
    def test_women_category_is_opened(self, browser, with_expect, _setup_page):
        with_expect(browser.locator(self.women_page.PAGE_TITLE)).to_be_visible()

    @allure.title("Shopping category options are visible and correct")
    @pytest.mark.parametrize('options_titles', [pytest.param(ParametrizationData.CLOTH_OPTIONS_TITLE,
                                                             id="Shopping Titles")])
    def test_shopping_options_on_tops(self, browser, options_titles, _setup_page):
        shopping_options = self.women_page.get_shopping_options_titles(self.base_locators.SHOP_OPTIONS_CATEGORY)
        assert options_titles == shopping_options, "'Shopping Options' are not matched!"

    @allure.title("The item is added to the cart")
    def test_add_item_to_cart(self, browser, _setup_page):
        self.women_page.choose_random_cloth()
        self.women_page.check_success_alert(self.base_locators.ALERT_SUCCESS)

    @allure.title("Items are sorted by price")
    def test_sort_items_by_price(self, browser, _setup_page):
        products_not_sorted = self.women_page.get_products_details()
        self.women_page.sort_products_by(self.PRICE)
        product_sorted_by_price = self.women_page.get_products_details()
        assert products_not_sorted != product_sorted_by_price
