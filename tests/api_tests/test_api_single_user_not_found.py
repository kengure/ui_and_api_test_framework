"""Тест кейс для API запроса single user not found"""
import allure
import pytest
from helper.load import load_data


@allure.parent_suite("API tests")
@allure.suite("api_single_user_not_found")
@allure.title("Запрос получения данных об отсутствии пользователя с валидным значением")
@pytest.mark.parametrize(
    ("user_id", "expected_data"), load_data("single_user_data", "not_found_data")
)
def test_api_single_user_not_found_parameters(reqres_api, user_id, expected_data):
    reqres_api.reqres_single_user(user_id).status_code_should_be(
        404
    ).have_value_in_response_parameter([], expected_data)
