"""Тест кейс для API запроса list users"""
import allure
import pytest

from helper.load import load_data


@allure.parent_suite("API tests")
@allure.suite("api_list_users")
@allure.title("Запрос получения данных списка пользователей")
@pytest.mark.parametrize(("page_num"), load_data("list_users_data"))
def test_api_list_users_valid_parameters(reqres_api, page_num):
    reqres_api.reqres_list_users(page_num).status_code_should_be(
        200
    ).json_schema_should_be_valid("list_users_schema").have_value_in_response_parameter(
        ["page"], page_num
    )
