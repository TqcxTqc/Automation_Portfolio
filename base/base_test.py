import pytest

from pages.women_catalog import WomenCatalogPage
from pages.men_catalog import MenCatalogPage
from config.data import Data
from config.locators_pytest_param import ClothColor, ClothSize, CommonLocators


class BaseTest:
    women_catalog: WomenCatalogPage
    men_catalog: MenCatalogPage
    data: Data
    cloth_color: ClothColor
    cloth_size: ClothSize
    common_locators: CommonLocators

    @pytest.fixture(autouse=True)
    def setup(self, request, browser):
        request.cls.browser = browser
        request.cls.women_catalog = WomenCatalogPage(browser)
        request.cls.men_catalog = MenCatalogPage(browser)
        request.cls.data = Data()
        request.cls.cloth_color = ClothColor()
        request.cls.cloth_size = ClothSize()
        request.cls.common_locators = CommonLocators()
