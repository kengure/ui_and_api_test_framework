"""Дата файл для тестирования api reqres, single user"""
from model.single_user_model import ResponseSingleUserModel

# user_id = 2
user_id_2 = ResponseSingleUserModel(
    id=2,
    email="janet.weaver@reqres.in",
    first_name="Janet",
    last_name="Weaver",
    avatar="https://reqres.in/img/faces/2-image.jpg",
    url="https://reqres.in/#support-heading",
    text="To keep ReqRes free, contributions towards server costs are appreciated!",
)

empty_data = {}

# Данные для тестов API ('user_id', 'expected_data')
data = ((2, user_id_2),)
not_found_data = ((23, empty_data),)

# Данные для тестов UI ('request_name', 'user_id')
ui_data = (("users-single", 2),)
ui_not_found_data = (("users-single-not-found", 23),)
