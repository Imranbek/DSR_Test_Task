# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture
def chrome_browser_context(browser):
    context = browser.new_context()
    yield context
    context.close()












    # chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    # browser_obj = webdriver.Chrome(options=chrome_options)
    # # browser_obj.implicitly_wait(10)
    # browser_obj.maximize_window()
    # browser_obj.delete_all_cookies()
    # yield browser_obj
    # browser_obj.quit()