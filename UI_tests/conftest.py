import pytest

pytest_plugins = [
    'conftest_browser',
    'conftest_cv_page'
]
@pytest.fixture(scope='session')
def cv_page_url():
    url = 'https://vladimirwork.github.io/web-ui-playground'
    return url
