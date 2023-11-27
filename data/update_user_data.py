"""Дата файл для тестирования запроса update user"""
from model.update_model import RequestUpdateUserModel

# данные для API тестов ('user_id', 'request_parameters')
data = ((2, RequestUpdateUserModel(name="morpheus", job="zion resident")),)

# данные для UI тестов patch ('request_name', 'user_id', 'request_parameters')
ui_data_patch = (
    ("patch", 2, RequestUpdateUserModel(name="morpheus", job="zion resident")),
)

# данные для UI тестов put ('request_name', 'user_id', 'request_parameters')
ui_data_put = (
    ("put", 2, RequestUpdateUserModel(name="morpheus", job="zion resident")),
)
