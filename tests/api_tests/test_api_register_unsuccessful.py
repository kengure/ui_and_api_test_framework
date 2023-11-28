"""Тест кейс для API запроса register unsuccessful """
import allure
import pytest
from helper.load import load_data


@allure.parent_suite("API tests")
@allure.suite("api_register_unsuccessful")
@allure.title("Запрос на регистрацию с невалидными параметрами")
@pytest.mark.parametrize(
    "request_parameters", load_data("register_data", "not_valid_data")
)
def test_api_register_unsuccessful_parameters(reqres_api, request_parameters):
    reqres_api.reqres_register(request_parameters).status_code_should_be(
        400
    ).json_schema_should_be_valid(
        "register_unsuccessful_schema"
    ).have_value_in_response_parameter(
        ["error"], "Missing password"
    )
