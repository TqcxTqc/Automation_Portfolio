import pytest

from pages.women_catalog import WomenCatalogPage
from pages.men_catalog import MenCatalogPage


class BaseTest:
    women_catalog: WomenCatalogPage
    men_catalog: MenCatalogPage

    @pytest.fixture(autouse=True)
    def setup(self, request, browser):
        request.cls.browser = browser
        request.cls.women_catalog = WomenCatalogPage(browser)
        request.cls.men_catalog = MenCatalogPage(browser)
