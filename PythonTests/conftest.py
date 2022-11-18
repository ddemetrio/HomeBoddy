import allure
import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def initial_driver():
    with allure.step('Старт браузера'):
        driver = webdriver.Chrome()
        driver.set_window_size(1024, 768)
    return driver
