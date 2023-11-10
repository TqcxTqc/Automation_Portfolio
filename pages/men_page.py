from base.base_page import BasePage
from pages.common.top_menu import TopMenuBar


class MenPage(BasePage):
    PAGE_URL = TopMenuBar.MEN_CATALOG

    # Category on page
    MEN_TOPS = "#narrow-by-list2 a[href*='tops-men']"
    MEN_BOTTOMS = "#narrow-by-list2 a[href*='bottoms-men']"

    # Tops items
    MEN_HOODIE_SWEATSHIRTS = ".categories-menu a[href*='hoodies-and-sweatshirts-men']"
    MEN_JACKETS = ".categories-menu a[href*='jackets-men']"
    MEN_TEES = ".categories-menu a[href*='tees-men']"
    MEN_BRAS_TANKS = ".categories-menu a[href*='tanks-men']"

    # Bottoms items
    MEN_PANTS = ".categories-menu a[href*='pants-men']"
    MEN_SHORTS = ".categories-menu a[href*='shorts-men']"
