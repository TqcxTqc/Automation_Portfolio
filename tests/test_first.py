import time

from base.base_test import BaseTest


class TestWomenCatalogFeatures(BaseTest):

    def test_women_tops_catalog(self, browser):
        self.women_catalog.open()
        self.women_catalog.click_on_category(self.women_catalog.WOMEN_SHORTS)
        time.sleep(2)
