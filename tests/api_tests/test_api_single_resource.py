"""Тест кейс для API запроса single resource"""
import allure
import pytest

from helper.load import load_data


@allure.parent_suite("API tests")
@allure.suite("api_single_resource")
@allure.title("Запрос получения данных о ресурсе с валидным значением")
@pytest.mark.parametrize(
    ("resource_id", "expected_data"), load_data("single_resource_data")
)
def test_api_single_resource_valid_parameters(reqres_api, resource_id, expected_data):
    reqres_api.reqres_single_resource(resource_id).status_code_should_be(
        200
    ).json_schema_should_be_valid("single_resource_schema").objects_should_be(
        expected_data, reqres_api.deserialize_single_resource()
    )
