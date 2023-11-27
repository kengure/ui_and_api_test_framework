"""Тест кейс для UI запроса single user"""
import allure
import pytest

from helper.load import load_data
from ui.page import ReqresUI


@allure.parent_suite("UI tests")
@allure.suite("ui_single_user")
@allure.title("Запрос получения данных пользователя с валидным значением")
@pytest.mark.parametrize(
    ("request_name", "user_id"), load_data("single_user_data", "ui_data")
)
def test_ui_single_user_valid_parameters(browser, reqres_api, request_name, user_id):
    reqres_main_page = ReqresUI(browser)
    with allure.step("Переходим на портал reqres.in и выполняем UI запрос"):
        ui_status_code, ui_response_json = reqres_main_page.run_ui_test(request_name)
    with allure.step("Выполняем api запрос"):
        api_status_code, api_response_json = reqres_api.reqres_single_user(
            user_id
        ).get_response()
    with allure.step("Проверяем, что response api и ui совпадают"):
        assert ui_status_code == api_status_code
        assert ui_response_json == str(api_response_json)
