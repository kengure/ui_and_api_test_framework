"""Дата файл для тестирования запроса register"""
from model.register_model import (RequestRegisterSuccessfulModel,
                                  RequestRegisterUnsuccessfulModel)

# данные для API тестов ('request_parameters')
data = (RequestRegisterSuccessfulModel(email="eve.holt@reqres.in", password="pistol"),)
not_valid_data = (RequestRegisterUnsuccessfulModel(email="sydney@fife"),)

# данные для тестов ('request_name', 'request_parameters')
ui_data = (
    (
        "register-successful",
        RequestRegisterSuccessfulModel(email="eve.holt@reqres.in", password="pistol"),
    ),
)
ui_not_valid_data = (
    ("register-unsuccessful", RequestRegisterUnsuccessfulModel(email="sydney@fife")),
)
