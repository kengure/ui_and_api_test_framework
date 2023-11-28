"""Тест кейс для API запроса login successful"""
import allure
import pytest
from helper.load import load_data


@allure.parent_suite("API tests")
@allure.suite("api_login_successful")
@allure.title("Запрос на авторизацию с валидными параметрами")
@pytest.mark.parametrize("request_parameters", load_data("login_data", "data"))
def test_api_login_valid_parameters(reqres_api, request_parameters):
    reqres_api.reqres_login(request_parameters).status_code_should_be(
        200
    ).json_schema_should_be_valid("login_successful_schema")
