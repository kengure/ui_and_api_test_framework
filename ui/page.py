"""Модуль для работы со страницей"""
from time import sleep

import allure
from selenium.webdriver.common.by import By

from ui.browser import Browser


class ReqresLocators:
    """Основной класс для локаторов"""

    REQRES_MAIN_PAGE = (
        By.XPATH,
        "//body//h1[@class = 'logo']//*[@src = '/img/logo.png']",
    )
    REQUEST_BUTTON = lambda request_name: (
        By.XPATH,
        f"//div[@class = 'endpoints']//li[@data-id = '{request_name}']/a",
    )
    ACTIVE_REQUEST = lambda request_name: (
        By.XPATH,
        f"//div[@class = 'endpoints']//li[@data-id = '{request_name}' and @class='active']/a",
    )
    RESPONSE = (By.XPATH, "//div[@class='output']//div[@class='response']")
    RESPONSE_STATUS_CODE = (
        By.XPATH,
        "//div[@class='output']//div[@class='response']//span[contains(@class, 'response-code')]",
    )
    RESPONSE_JSON = (
        By.XPATH,
        "//div[@class='output']//div[@class='response']//pre[@data-key='output-response' and not(@hidden)]",
    )


class ReqresUI(Browser):
    """Основной класс для работы с UI элементами"""

    @allure.step("Ожидание, что основная страница видна")
    def wait_until_main_page_is_displayed(self, timeout=Browser._DEFAULT_TIMEOUT):
        assert self.find_element(
            ReqresLocators.REQRES_MAIN_PAGE, time=timeout
        ).is_displayed()
        return self

    @allure.step("Отправка запроса через UI")
    def send_request(self, request_name, timeout=Browser._DEFAULT_TIMEOUT):
        assert self.find_element(
            ReqresLocators.REQUEST_BUTTON(request_name), time=timeout
        ).is_displayed()
        self.find_element(
            ReqresLocators.REQUEST_BUTTON(request_name), time=timeout
        ).click()
        sleep(1)
        assert self.find_element(
            ReqresLocators.ACTIVE_REQUEST(request_name), time=timeout
        ).is_displayed()
        return self

    @allure.step("Ожидание, что ответ на запрос виден")
    def wait_until_response_is_displayed(self, timeout=Browser._DEFAULT_TIMEOUT):
        assert self.find_element(ReqresLocators.RESPONSE, time=timeout).is_displayed()
        return self

    @allure.step("Ожидание, что код ответа виден")
    def wait_until_response_code_is_displayed(self, timeout=Browser._DEFAULT_TIMEOUT):
        assert self.find_element(ReqresLocators.RESPONSE_STATUS_CODE, time=timeout).is_displayed()
        return self

    @allure.step("Выполняем ui тест")
    def go_to_reqres_and_send_request_by_ui(self, request_name):
        with allure.step("Переходим на портал reqres.in"):
            self.go_to_reqres()
            self.wait_until_main_page_is_displayed()
        with allure.step("Выполняем ui запрос"):
            self.send_request(request_name)
        with allure.step("Проверяем, что код ответа и response видны"):
            self.wait_until_response_code_is_displayed()
            self.wait_until_response_is_displayed()
        with allure.step("Возвращаем response"):
            return self.get_responce_status_code(), self.get_response_json()

    @allure.step("Возвращаем код ответа")
    def get_responce_status_code(self, timeout=Browser._DEFAULT_TIMEOUT):
        return int(
            self.find_element(ReqresLocators.RESPONSE_STATUS_CODE, time=timeout).text
        )

    @allure.step("Возвращаем json ответа")
    def get_response_json(self, timeout=Browser._DEFAULT_TIMEOUT):
        response = (
            self.find_element(ReqresLocators.RESPONSE_JSON, time=timeout)
            .text.replace("\n", "")
            .replace('"', "'")
        )
        while "  " in response:
            response = response.replace("  ", " ")
        response = (
            response.replace("{ ", "{")
            .replace(" }", "}")
            .replace("[ ", "[")
            .replace(" ]", "]")
        )
        return response
