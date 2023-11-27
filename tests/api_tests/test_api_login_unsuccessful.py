"""Тест кейс для API запроса login unsuccessful"""
import allure
import pytest

from helper.load import load_data


@allure.parent_suite("API tests")
@allure.suite("api_login_unsuccessful")
@allure.title("Запрос на авторизацию с невалидными параметрами")
@pytest.mark.parametrize(
    "request_parameters", load_data("login_data", "not_valid_data")
)
def test_api_login_unsuccessful_parameters(reqres_api, request_parameters):
    reqres_api.reqres_login(request_parameters).status_code_should_be(
        400
    ).json_schema_should_be_valid(
        "login_unsuccessful_schema"
    ).have_value_in_response_parameter(
        ["error"], "Missing password"
    )
