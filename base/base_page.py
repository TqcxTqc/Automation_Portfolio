import random


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self):
        """
        Open the page
        """
        self.browser.goto(self.PAGE_URL)

    def is_opened(self, title_selector):
        """
        Checking that page is loaded
        """
        self.browser.wait_for_load_state("networkidle")
        self.browser.wait_for_selector(title_selector)
        self.browser.is_visible(title_selector)

    def click_on_category(self, category):
        """
        Taking category locator and click selected category
        """
        self.browser.locator(category).click()

    def get_shopping_options_titles(self, locator_items):
        get_items_title = self.browser.query_selector_all(locator_items)
        return [element.text_content() for element in get_items_title]

    def choose_random_cloth(self, max_attempts=3):
        """
        Choose a random clothing product, color, and size.

        Args:
        max_attempts (int, optional): The maximum number of attempts to choose a product before
        considering the operation as failed. Default is 3.

        Raises:
            Exception: Raised when no products are found on the web page or if an issue occurs during
        product selection
        """
        for _ in range(max_attempts):
            try:
                products = self.browser.locator(".price-box.price-final_price").all()
                if not products:
                    raise Exception("No products found")

                # Choose a random product
                random_product_element = random.choice(products)
                product_id = random_product_element.get_attribute("data-product-id")
                print(f"Chosen product ID: {product_id}")

                # Choose a random size
                sizes = self.browser.locator(f".swatch-opt-{product_id} .swatch-option.text").all()
                if not sizes:
                    raise Exception("No sizes found")
                else:
                    random_size = random.choice(sizes)
                    random_size.click()
                    print("Selected a random size")

                # Choose a random color
                colors = self.browser.locator(f".swatch-opt-{product_id} .swatch-option.color").all()
                if not colors:
                    raise Exception("No colors found")
                else:
                    random_color = random.choice(colors)
                    random_color.click()
                    print("Selected a random color")
                    self.browser.wait_for_timeout(500)

                self.browser.locator(f"form[action*='/{product_id}/'] button").click()

                # Break out of the loop since we successfully selected a product
                break
            except Exception as e:
                # Handle any specific exceptions that may occur during the selection process
                print(f"Error while choosing product: {e}")

    def check_success_alert(self, alert):
        self.browser.wait_for_selector(alert).is_visible()
        if "You added" in self.browser.locator(alert).text_content():
            return True
        else:
            raise Exception("Product is not added")
