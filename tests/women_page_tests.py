import random
import time

import pytest

from base.base_test import BaseTest
from config.locators_pytest_param import ParametrizationData


class TestWomenCatalogFeatures(BaseTest):
    # Locators
    PAGE_TITLE = "#page-title-heading"

    def test_women_tops_catalog_is_opened(self, browser):
        self.women_catalog.open()
        self.women_catalog.click_on_category(self.women_catalog.WOMEN_TOPS)
        self.women_catalog.is_opened(self.PAGE_TITLE)

    @pytest.mark.parametrize('options_title', [ParametrizationData.CLOTH_OPTIONS_TITLE])
    def test_shopping_options_on_tops(self, browser, with_expect, options_title):
        self.women_catalog.open()
        self.women_catalog.click_on_category(self.women_catalog.WOMEN_TOPS)
        self.women_catalog.is_opened(self.PAGE_TITLE)
        shopping_options = self.women_catalog.get_shopping_options_titles(
            "#narrow-by-list div .filter-options-title")
        assert options_title == shopping_options, "'Shopping Options' are not matched"

    def test_add_item_to_cart(self, browser):
        self.women_catalog.open()
        self.women_catalog.click_on_category(self.women_catalog.WOMEN_TOPS)
        browser.goto("https://magento.softwaretestingboard.com/women/tops-women.html")
        self.women_catalog.choose_random_cloth()
        self.women_catalog.check_success_alert(self.common_locators.ALERT_SUCCESS)
