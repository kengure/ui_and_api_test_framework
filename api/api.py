"""Модуль для работы с api, отправка http запросов и получение ответов"""

import allure
import requests
from jsonschema import validate

from helper.load import load_json_schema
from helper.parser import get_data


class Api:
    """Основной класс для работы с Api"""

    _HEADERS = {"Content-Type": "application/json; charset=utf-8"}
    _TIMEOUT = 10

    def __init__(self):
        self.response = None

    @allure.step("Отправить POST запрос")
    def post(
        self, url: str, endpoint: str, params: dict = None, json_body: dict = None
    ):
        with allure.step(
            f"POST запрос на url: {url}{endpoint}" f"\n тело запроса: \n {json_body}"
        ):
            self.response = requests.post(
                url=f"{url}{endpoint}",
                headers=self._HEADERS,
                params=params,
                json=json_body,
                timeout=self._TIMEOUT,
            )
        return self

    @allure.step("Отправить PUT запрос")
    def put(self, url: str, endpoint: str, params: dict = None, json_body: dict = None):
        with allure.step(
            f"PUT запрос на url: {url}{endpoint}" f"\n тело запроса: \n {json_body}"
        ):
            self.response = requests.put(
                url=f"{url}{endpoint}",
                headers=self._HEADERS,
                params=params,
                json=json_body,
                timeout=self._TIMEOUT,
            )
        return self

    @allure.step("Отправить PATCH запрос")
    def patch(
        self, url: str, endpoint: str, params: dict = None, json_body: dict = None
    ):
        with allure.step(
            f"PATCH запрос на url: {url}{endpoint}" f"\n тело запроса: \n {json_body}"
        ):
            self.response = requests.patch(
                url=f"{url}{endpoint}",
                headers=self._HEADERS,
                params=params,
                json=json_body,
                timeout=self._TIMEOUT,
            )
        return self

    @allure.step("Отправить GET запрос")
    def get(self, url: str, endpoint: str):
        with allure.step(f"GET запрос на url: {url}{endpoint}"):
            self.response = requests.get(
                url=f"{url}{endpoint}", headers=self._HEADERS, timeout=self._TIMEOUT
            )
        return self

    @allure.step("Отправить DELETE запрос")
    def delete(self, url: str, endpoint: str):
        with allure.step(f"DELETE запрос на url: {url}{endpoint}"):
            self.response = requests.get(
                url=f"{url}{endpoint}", headers=self._HEADERS, timeout=self._TIMEOUT
            )
        return self

    ### ASSERTIONS ###
    @allure.step("Статус код ответа равен {expected_code}")
    def status_code_should_be(self, expected_code: int):
        """Проверяем статус код ответа actual_code на соответствие expected_code"""
        actual_code = self.response.status_code
        assert expected_code == actual_code, (
            f"\nОжидаемый результат: {expected_code} "
            f"\nФактический результат: {actual_code}"
        )
        return self

    @allure.step("Cхема ответа json валидна")
    def json_schema_should_be_valid(
        self, path_json_schema: str, name_json_schema: str = "schema"
    ):
        """Проверяем полученный ответ на соответствие json схеме"""
        json_schema = load_json_schema(path_json_schema, name_json_schema)
        validate(self.response.json(), json_schema)
        return self

    @allure.step("Объекты равны")
    def objects_should_be(self, expected_object, actual_object):
        """Сравниваем два объекта"""
        assert expected_object == actual_object, (
            f"\nОжидаемый результат: {expected_object} "
            f"\nФактический результат: {actual_object}"
        )
        return self

    @allure.step("В поле ответа содержится искомое значение")
    def have_value_in_response_parameter(self, keys: list, value: str):
        """Сравниваем значение необходимого параметра"""
        payload = self.get_payload(keys)
        assert value == payload, (
            f"\nОжидаемый результат: {value} " f"\nФактический результат: {payload}"
        )
        return self

    ### Getters ###
    def get_payload(self, keys: list):
        """Получаем payload переходя по ключам,
        и возвращаем полученный payload"""
        response = self.response.json()
        payload = get_data(keys, response)
        return payload

    @allure.step("Возвращаем код ответа и response")
    def get_response(self):
        """Возвращаем response"""
        return self.response.status_code, self.response.json()
