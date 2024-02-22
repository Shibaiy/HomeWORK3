import pytest
from selene import browser

@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.window_width = 1080
    browser.config.window_height = 800
    browser.open('https://demoqa.com/automation-practice-form/')

    yield

    browser.quit()
