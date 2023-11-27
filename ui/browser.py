"""Модуль для работы с браузером"""
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Browser:
    """Основной класс для работы с браузером"""

    _URL = "https://reqres.in/"
    _DEFAULT_TIMEOUT = 10

    def __init__(self, driver, base_url=_URL):
        self.driver = driver
        self.base_url = base_url

    @allure.step("Поиск элемента")
    def find_element(self, locator, time=_DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    @allure.step("Переход на портал reqres.in")
    def go_to_reqres(self):
        return self.driver.get(self.base_url)
