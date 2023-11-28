"""Тест кейс для API запроса create user"""
import allure
import pytest
from helper.load import load_data


@allure.parent_suite("API tests")
@allure.suite("api_create_user")
@allure.title("Запрос на создание пользователя")
@pytest.mark.parametrize("request_parameters", load_data("create_user_data", "data"))
def test_api_create_user_with_valid_parameters(reqres_api, request_parameters):
    reqres_api.reqres_create(request_parameters).status_code_should_be(
        201
    ).json_schema_should_be_valid(
        "create_user_schema"
    ).have_value_in_response_parameter(
        ["name"], request_parameters.name
    )
