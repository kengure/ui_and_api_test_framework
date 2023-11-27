"""Тест кейс для запроса update user через put"""
import allure
import pytest

from helper.load import load_data


@allure.parent_suite("API tests")
@allure.suite("api_update_user_by_put")
@allure.title("Запрос на обновление данных пользователя")
@pytest.mark.parametrize(
    ("user_id", "request_parameters"), load_data("update_user_data")
)
def test_update_user_with_put_by_parameters(reqres_api, user_id, request_parameters):
    reqres_api.reqres_update_by_put(user_id, request_parameters).status_code_should_be(
        200
    ).have_value_in_response_parameter(
        ["name"], request_parameters.name
    ).have_value_in_response_parameter(
        ["job"], request_parameters.job
    )
