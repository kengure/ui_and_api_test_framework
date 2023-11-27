"""Тест кейс для UI запроса login successful"""
import allure
import pytest

from helper.load import load_data
from ui.page import ReqresUI


@allure.parent_suite("UI tests")
@allure.suite("ui_login_successful")
@allure.title("Запрос на авторизацию с валидными параметрами")
@pytest.mark.parametrize(
    ("request_name", "request_parameters"), load_data("login_data", "ui_data")
)
def test_ui_login_valid_parameters(
    browser, reqres_api, request_name, request_parameters
):
    reqres_main_page = ReqresUI(browser)
    with allure.step("Переходим на портал reqres.in и выполняем UI запрос"):
        ui_status_code, ui_response_json = reqres_main_page.run_ui_test(request_name)
    with allure.step("Выполняем api запрос"):
        api_status_code, api_response_json = reqres_api.reqres_login(
            request_parameters
        ).get_response()
    with allure.step("Проверяем, что response api и ui совпадают"):
        assert ui_status_code == api_status_code
        assert ui_response_json == str(api_response_json)
