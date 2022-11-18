from __future__ import annotations

from typing import Optional

from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasicMethods:
    """Базовые методы UI тестов"""

    def __init__(self, driver):
        self.driver = driver

    def get_url(self, url: str) -> BasicMethods:
        """ Функция позволяет перейти по нужному адресу
        Args:
            url: адрес в браузере
        """
        self.driver.get(url)
        return self

    def element_presence(self, locator: tuple[str, str], driver: Optional[WebDriver | WebElement] = None,
                         message: Optional[str] = None, waiting_time: int = 10) -> WebElement:
        """ Функция на поиск элемента на странице
        Args:
            locator: локатор элемента
            driver: драйвер
            message: сообщение об ошибке
            waiting_time: время ожидания элемента
        """
        driver = self.driver if not driver else driver
        message = f"Can't find element by the locator {locator}" if not message else message
        return WebDriverWait(driver, waiting_time).until(EC.presence_of_element_located(locator), message=message)

    def list_of_elements_presence(self, locator: tuple[str, str], driver: Optional[WebDriver | WebElement] = None,
                                  message: Optional[str] = None, waiting_time: int = 10) -> list[WebElement]:
        """ Функция на поиск всех подходящих элементов
        Args:
            locator: локатор элемента
            driver: драйвер
            message: сообщение об ошибке
            waiting_time: время ожидания элемента
        """
        driver = self.driver if not driver else driver
        message = f"Can't find element by the locator {locator}" if not message else message
        return WebDriverWait(driver, waiting_time).until(EC.presence_of_all_elements_located(locator), message=message)
