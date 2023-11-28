"""Тест кейс для UI запроса list users with delay"""
import allure
import pytest
from helper.load import load_data
from ui.page import ReqresUI


@allure.parent_suite("UI tests")
@allure.suite("ui_list_users_with_delay")
@allure.title("Запрос получения данных списка пользователей с задержкой")
@pytest.mark.parametrize(
    ("request_name", "delay"), load_data("list_users_data", "ui_delay_data")
)
def test_ui_list_users_with_delay_valid_parameters(
    browser, reqres_api, request_name, delay
):
    reqres_main_page = ReqresUI(browser)
    with allure.step("Переходим на портал reqres.in и выполняем UI запрос"):
        (
            ui_status_code,
            ui_response_json,
        ) = reqres_main_page.go_to_reqres_and_send_request_by_ui(request_name)
    with allure.step("Выполняем api запрос"):
        api_status_code, api_response_json = reqres_api.reqres_list_users_with_delay(
            delay
        ).get_response()
    with allure.step("Проверяем, что response api и ui совпадают"):
        assert ui_status_code == api_status_code
        assert ui_response_json == str(api_response_json)
