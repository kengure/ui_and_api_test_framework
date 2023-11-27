"""Дата файл для тестирования запроса Login"""
from model.login_model import (RequestLoginSuccessfulModel,
                               RequestLoginUnsuccessfulModel)

# данные для API тестов ('request_parameters')
data = (RequestLoginSuccessfulModel(email="eve.holt@reqres.in", password="cityslicka"),)
not_valid_data = (RequestLoginUnsuccessfulModel(email="sydney@fife"),)

# данные для UI тестов ('requset_name','request_parameters')
ui_data = (
    (
        "login-successful",
        RequestLoginSuccessfulModel(email="eve.holt@reqres.in", password="cityslicka"),
    ),
)
ui_not_valid_data = (
    ("login-unsuccessful", RequestLoginUnsuccessfulModel(email="sydney@fife")),
)
