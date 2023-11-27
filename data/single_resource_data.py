"""Дата файл для тестирования запроса single resource"""
from model.single_resource_model import ResponseSingleResourceModel

# resource_id = 2
resource_id_2 = ResponseSingleResourceModel(
    id=2, name="fuchsia rose", year=2001, color="#C74375", pantone_value="17-2031"
)

# пустое тело ответа
empty_data = {}

# Данные для API тестов ('resource_id', 'expected_data')
data = ((2, resource_id_2),)
not_valid_data = ((23, empty_data),)

# Данные для UI тестов ('request_name', 'resource_id')
ui_data = (("unknown-single", 2),)
ui_not_valid_data = (("unknown-single-not-found", 23),)
