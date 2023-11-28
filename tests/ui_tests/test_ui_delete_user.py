"""Тест кейс для UI запроса delete user"""
import allure
import pytest
from helper.load import load_data
from ui.page import ReqresUI


@allure.parent_suite("UI tests")
@allure.suite("ui_delete_user")
@allure.title("Запрос на создание пользователя")
@pytest.mark.parametrize(
    ("request_name", "user_id"), load_data("delete_user_data", "ui_data")
)
def test_ui_delete_user(browser, reqres_api, request_name, user_id):
    reqres_main_page = ReqresUI(browser)
    with allure.step("Переходим на портал reqres.in и выполняем UI запрос"):
        (
            ui_status_code,
            ui_response_json,
        ) = reqres_main_page.go_to_reqres_and_send_request_by_ui(request_name)
    with allure.step("Выполняем api запрос"):
        api_status_code, api_response_json = reqres_api.reqres_delete(
            user_id
        ).get_response()
    with allure.step("Проверяем, что response api и ui совпадают"):
        # Периодически UI возвращает код 204 вместо 200
        assert ui_status_code == api_status_code
        assert ui_response_json == str(api_response_json)
