import os
import pytest
import allure

from config.logger import setup_logger
from config.allure_config import add_allure_env
from playwright.sync_api import sync_playwright, expect, Error

LOGGER = setup_logger(__name__)


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chromium",
                     help="Specify browser: -firefox, -chromium, -webkit")
    parser.addoption("--head", action="store_false",
                     help="Launched in headless mode: if specified then launched in headed mode")


@pytest.hookimpl(tryfirst=True)
def pytest_exception_interact(call):
    # Check if the exception is a Playwright Error
    if isinstance(call.excinfo.value, Error):
        # Create a logfile
        LOGGER.exception(f"Error occurred during playwright execution: {call.excinfo.typename} / {call.excinfo.value}")

    # Log other exceptions raised during pytest execution
    LOGGER.exception(f"Error occurred during pytest execution:{call.excinfo.typename} / {call.excinfo.value}")


@pytest.fixture(scope="session")
def call_playwright():
    with sync_playwright() as playwright:
        yield playwright
        playwright.stop()


@pytest.fixture()
def browser(call_playwright, request):
    head = request.config.getoption("--head")
    browser = request.config.getoption("--browser_name")
    if head:
        headless = True
    else:
        headless = False

    LOGGER.info(f"Launching {browser} browser in {'headless' if headless else 'headed'} mode.")

    if browser == "chromium":
        driver = call_playwright.chromium.launch(headless=headless)
    elif browser == "firefox":
        driver = call_playwright.firefox.launch(headless=headless)
    elif browser == "webkit":
        driver = call_playwright.webkit.launch(headless=headless)
    else:
        LOGGER.error("Unsupported browser type")
        assert False, "Unsupported browser type"

    context = driver.new_context()
    context.set_default_timeout(10000)
    page = context.new_page()

    add_allure_env(context)

    yield page
    page.close()
    context.close()
    driver.close()


@pytest.fixture()
def with_expect():
    return expect


@pytest.fixture(autouse=True)
def screenshot_on_failure(request, browser):
    yield
    if request.node.rep_call.failed:
        screenshot_path = os.path.join("reports", "screenshots", f"{request.node.name}_screenshot.png")
        allure.attach(body=browser.screenshot(path=screenshot_path, full_page=True),
                      attachment_type=allure.attachment_type.PNG)
