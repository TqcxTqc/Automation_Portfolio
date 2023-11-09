import pytest

from pages.women_page import WomenPage
from pages.men_page import MenPage
from config.data import Data
from config.locators_pytest_param import ClothColor, ClothSize, BaseLocators


class BaseTest:
    women_page: WomenPage
    men_page: MenPage
    data: Data
    cloth_color: ClothColor
    cloth_size: ClothSize
    base_locators: BaseLocators

    @pytest.fixture(autouse=True)
    def setup(self, request, browser):
        request.cls.browser = browser
        request.cls.women_page = WomenPage(browser)
        request.cls.men_page = MenPage(browser)
        request.cls.data = Data()
        request.cls.cloth_color = ClothColor()
        request.cls.cloth_size = ClothSize()
        request.cls.base_locators = BaseLocators()
