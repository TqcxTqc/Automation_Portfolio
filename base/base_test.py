import pytest

from pages.women_page import WomenPage
from pages.men_page import MenPage
from config.data import Data
from config.locators_pytest_param import ClothColor, ClothSize, BaseLocators
from config.logger import setup_logger


class BaseTest:
    LOGGER_MESSAGE = "FROM TEST ==>"

    women_page: WomenPage
    men_page: MenPage
    data: Data
    cloth_color: ClothColor
    cloth_size: ClothSize
    base_locators: BaseLocators
    logger: setup_logger(__name__)

    @pytest.fixture(autouse=True)
    def setup(self, request, browser):
        request.cls.browser = browser
        request.cls.women_page = WomenPage(browser)
        request.cls.men_page = MenPage(browser)
        request.cls.data = Data()
        request.cls.cloth_color = ClothColor()
        request.cls.cloth_size = ClothSize()
        request.cls.base_locators = BaseLocators()
        request.cls.logger = setup_logger(self.LOGGER_MESSAGE)
