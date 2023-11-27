"""Тест кейс для API запроса single user"""
import allure
import pytest

from helper.load import load_data


@allure.parent_suite("API tests")
@allure.suite("api_single_user")
@allure.title("Запрос получения данных пользователя с валидным значением")
@pytest.mark.parametrize(("user_id", "expected_data"), load_data("single_user_data"))
def test_api_single_user_valid_parameters(reqres_api, user_id, expected_data):
    reqres_api.reqres_single_user(user_id).status_code_should_be(
        200
    ).json_schema_should_be_valid("single_user_schema").objects_should_be(
        expected_data, reqres_api.deserialize_single_user()
    )
