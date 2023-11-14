import random
import allure


class BasePage:
    PAGE_TITLE = "#page-title-heading"

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        """
        Open the page
        """
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.browser.goto(self.PAGE_URL)

    def is_opened(self, title_selector):
        """
        Checking that page is loaded
        """
        with allure.step(f"Page {self.PAGE_URL} is opened"):
            self.browser.wait_for_load_state()
            self.browser.wait_for_selector(title_selector)
            with allure.step(f"Title is visible {title_selector}"):
                self.browser.is_visible(title_selector)

    def click_on_category(self, category):
        """
        Taking category locator and click selected category
        """
        with allure.step(f"Clicked on {category}"):
            self.browser.locator(category).click()

    @allure.step("Taking shopping titles")
    def get_shopping_options_titles(self, locator_items):
        self.browser.wait_for_selector(locator_items)
        get_items_title = self.browser.query_selector_all(locator_items)
        return [element.text_content() for element in get_items_title]

    @allure.step("Select random cloth")
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
                self.browser.wait_for_load_state()
                products = self.browser.locator(".price-box.price-final_price").all()
                if not products:
                    raise Exception("No products found")

                # Choose a random product
                random_product_element = random.choice(products)
                product_id = random_product_element.get_attribute("data-product-id")
                print(f"Chosen product ID: {product_id}")
                self.browser.wait_for_selector(f".swatch-opt-{product_id}")

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

    @allure.step("Check success alert")
    def check_success_alert(self, alert):
        self.browser.wait_for_selector(alert).is_visible()
        if "You added" in self.browser.locator(alert).text_content():
            return True
        else:
            raise Exception("Product is not added")

    def sort_products_by(self, sort_type, timeout=3000):
        with allure.step(f"Sorting products by: {sort_type}"):
            self.browser.locator("#sorter").first.select_option(sort_type)

            # Wait for the sorting to be applied (You can adjust the wait time based on your needs)
            self.browser.wait_for_timeout(timeout)

            # Check if the product items are visible
            product_items = self.browser.locator(".product-items")
            if not product_items.is_visible():
                # Handle the case where the product items are not visible
                self.browser.reload()
                self.browser.wait_for_load_state()

                # Wait for the sorting to be applied again
                self.browser.wait_for_timeout(timeout)

                # Check if the product items are visible again
                if not product_items.is_visible():
                    # Handle the case where the items are still not visible (e.g., raise an exception)
                    raise Exception("Product items are still not visible after refresh.")

    @allure.step("Getting products details")
    def get_products_details(self):
        """
        Retrieve product details from a web page.
        This method locates and extracts product names and prices from the web page.

        Returns:
        Tuple of two lists:
        - List of product names.
        - List of product prices.
        """
        name = ".product-item-details a.product-item-link"
        price = ".product-item-details span.price"
        product_name = self.browser.locator(name).all()
        product_price = self.browser.locator(price).all()
        product_name_list = [item.text_content().replace("\n", "").strip() for item in product_name]
        product_price_list = [item.text_content().replace("\n", "").strip() for item in product_price]
        return product_name_list, product_price_list
