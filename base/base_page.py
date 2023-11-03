class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self):
        """
        Open the page
        """
        self.browser.goto(self.PAGE_URL)

    def is_opened(self):
        """
        Checking that page is loaded
        """
        self.browser.wait_for_load_state()

    def click_on_category(self, category):
        """
        Taking category locator and click selected category
        """
        self.browser.locator(category).click()
