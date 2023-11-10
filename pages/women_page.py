from base.base_page import BasePage
from pages.common.top_menu import TopMenuBar


class WomenPage(BasePage):
    PAGE_URL = TopMenuBar.WOMEN_CATALOG

    # Category on page
    WOMEN_TOPS = "#narrow-by-list2 a[href*='tops-women']"
    WOMEN_BOTTOMS = "#narrow-by-list2 a[href*='bottoms-women']"

    # Tops items
    WOMEN_HOODIE_SWEATSHIRTS = ".categories-menu a[href*='hoodies-and-sweatshirts-women']"
    WOMEN_JACKETS = ".categories-menu a[href*='jackets-women']"
    WOMEN_TEES = ".categories-menu a[href*='tees-women']"
    WOMEN_BRAS_TANKS = ".categories-menu a[href*='tanks-women']"

    # Bottoms items
    WOMEN_PANTS = ".categories-menu a[href*='pants-women']"
    WOMEN_SHORTS = ".categories-menu a[href*='shorts-women']"
