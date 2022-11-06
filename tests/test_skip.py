import pytest
from selene import have
from selene.support.shared import browser
from tests import settings


@pytest.fixture(params=[(1980, 1024), (900, 600)], ids=['desktop', 'mobile'])
def browser_config(request):
    browser.config.window_width = request.param[0]
    browser.config._window_height = request.param[1]
    browser.open('https://github.com')
    yield


def test_browser(browser_config):
    if (browser.config.window_width, browser.config.window_height) not in settings.desktop:
        pytest.skip('Тест пропущен,тк не относится к тестированию desktop')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.should(have.url('https://github.com/login'))


def test_mobile_browser(browser_config):
    if (browser.config.window_width, browser.config.window_height) not in settings.mobile:
        pytest.skip('Тест пропущен,тк не относится к тестированию  mobile')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.should(have.url('https://github.com/login'))
