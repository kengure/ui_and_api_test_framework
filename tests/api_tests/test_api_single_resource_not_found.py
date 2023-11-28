"""Тест кейс для API запроса single resource not found"""
import allure
import pytest
from helper.load import load_data


@allure.parent_suite("API tests")
@allure.suite("api_single_resource_not_found")
@allure.title("Запрос получения данных ресурса с невалидным значением")
@pytest.mark.parametrize(
    ("resource_id", "expected_data"),
    load_data("single_resource_data", "not_valid_data"),
)
def test_api_single_resource_not_found_parameters(
    reqres_api, resource_id, expected_data
):
    reqres_api.reqres_single_resource(resource_id).status_code_should_be(
        404
    ).have_value_in_response_parameter([], expected_data)
