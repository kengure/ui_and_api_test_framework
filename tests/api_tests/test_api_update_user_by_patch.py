"""Тест кейс для API запроса update user через patch"""
import allure
import pytest
from helper.load import load_data


@allure.parent_suite("API tests")
@allure.suite("api_update_user_by_patch")
@allure.title("Запрос на обновление данных пользователя через patch")
@pytest.mark.parametrize(
    ("user_id", "request_parameters"), load_data("update_user_data")
)
def test_api_update_user_by_patch_with_parameters(
    reqres_api, user_id, request_parameters
):
    reqres_api.reqres_update_by_patch(
        user_id, request_parameters
    ).status_code_should_be(200).have_value_in_response_parameter(
        ["name"], request_parameters.name
    ).have_value_in_response_parameter(
        ["job"], request_parameters.job
    )
