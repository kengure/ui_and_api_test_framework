"""Тест кейс для API запроса list resource"""
import allure
import pytest


@allure.parent_suite("API tests")
@allure.suite("api_list_resource")
@allure.title("Запрос получения данных списка ресурсов")
def test_api_list_resource_valid_parameters(reqres_api):
    reqres_api.reqres_list_resource().status_code_should_be(
        200
    ).json_schema_should_be_valid("list_resource_schema")
