import pytest
from ..resources.pageObjects.HomePage import HomePage


@pytest.fixture(scope='session')
def create_browser_context(browser) -> None:
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    page.goto("https://www.ah.nl")
    # created this context for reusing auth state by loggin in
    # code for auth state goes in here

    context.storage_state(path="auth_state/state.json")
    yield context


@pytest.fixture()
def set_up(create_browser_context, browser) -> None:
    context = browser.new_context(storage_state="auth_state/state.json")
    page = context.new_page()
    homepage = HomePage(page)

    page.goto("https://www.ah.nl")
    page.set_viewport_size({"width": 1700, "height": 1024})
    if homepage.cookies_popup.is_visible():
        homepage.accept_cookies()
    yield page
    context.close()


