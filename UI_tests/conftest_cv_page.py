import pytest

from UI_tests.helpers.cv_page import CV_Page


@pytest.fixture
def cv_page(cv_page_url: str, chrome_browser_context):
    page = CV_Page(chrome_browser_context, cv_page_url)
    page.open()

    return page
