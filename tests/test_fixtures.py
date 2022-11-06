import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function')
def desktop_fixture():
    browser.config.window_width = 1980
    browser.config.window_height = 1024
    yield


@pytest.fixture(scope='function')
def mobile_fixture():
    browser.config.window_width = 900
    browser.config.window_height = 600
    yield


def test_browser(desktop_fixture):
    browser.open_url('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()


def test_mobile_browser(mobile_fixture):
    browser.open_url('https://github.com/')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
