"""Тест кейс для API запроса delete user"""
import allure
import pytest

from helper.load import load_data


@allure.parent_suite("API tests")
@allure.suite("api_delete_user")
@allure.title("Удаление пользователя")
@pytest.mark.parametrize(("user_id", "status"), load_data("delete_user_data"))
def test_api_delete_user(reqres_api, user_id, status):
    reqres_api.reqres_delete(user_id).status_code_should_be(status)
