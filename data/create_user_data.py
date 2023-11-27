"""Дата файл для тестирования запроса create user"""
from model.create_model import RequestCreateUserModel

# данные для API тестов ('request_parameters')
data = (RequestCreateUserModel(name="morpheus", job="leader"),)

# данные для UI тестов ('request_name', 'request_parameters')
ui_data = (("post", RequestCreateUserModel(name="morpheus", job="leader")),)
