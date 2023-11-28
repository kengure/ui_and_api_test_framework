"""Тест кейс для API запроса list users with delay"""
import allure
import pytest
from helper.load import load_data


@allure.parent_suite("API tests")
@allure.suite("api_list_users_with_delay")
@allure.title("Запрос получения данных списка пользователей с задержкой")
@pytest.mark.parametrize(("delay"), load_data("list_users_data", "api_delay_data"))
def test_api_list_users_with_delay_valid_parameters(reqres_api, delay):
    reqres_api.reqres_list_users_with_delay(delay).status_code_should_be(
        200
    ).json_schema_should_be_valid("list_users_schema")
