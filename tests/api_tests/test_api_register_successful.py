"""Тест кейс для API запроса register successful"""
import allure
import pytest

from helper.load import load_data


@allure.parent_suite("API tests")
@allure.suite("api_register_successful")
@allure.title("Запрос на регистрацию с валидными параметрами")
@pytest.mark.parametrize("request_parameters", load_data("register_data", "data"))
def test_api_register_valid_parameters(reqres_api, request_parameters):
    reqres_api.reqres_register(request_parameters).status_code_should_be(
        200
    ).json_schema_should_be_valid("register_successful_schema")
