"""Тест кейс для UI запроса update user через put"""
import allure
import pytest
from helper.load import load_data
from ui.page import ReqresUI


@allure.parent_suite("UI tests")
@allure.suite("ui_update_user_by_put")
@allure.title("Запрос на обновление данных пользователя через put")
@pytest.mark.parametrize(
    ("request_name", "user_id", "request_parameters"),
    load_data("update_user_data", "ui_data_put"),
)
def test_ui_update_user_by_put_with_parameters(
    browser, reqres_api, request_name, user_id, request_parameters
):
    reqres_main_page = ReqresUI(browser)
    with allure.step("Переходим на портал reqres.in и выполняем UI запрос"):
        (
            ui_status_code,
            ui_response_json,
        ) = reqres_main_page.go_to_reqres_and_send_request_by_ui(request_name)
    with allure.step("Выполняем api запрос"):
        api_status_code, api_response_json = reqres_api.reqres_update_by_put(
            user_id, request_parameters
        ).get_response()
    with allure.step("Проверяем, что response api и ui совпадают"):
        assert ui_status_code == api_status_code
        # ui_response_json и api_response_json для запроса update user через put не сравнить,
        # так как свойство 'createdAt' при каждом запросе имеет разные значения.
