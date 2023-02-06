import pytest
from appium import webdriver

import settings


@pytest.fixture(scope='class')
def driver():
    with webdriver.Remote(settings.APPIUM_SERVER_HOST, settings.DES_CAPS) as session:
        session.implicitly_wait(5)
        yield session

if __name__ == '__main__':

    print(driver)