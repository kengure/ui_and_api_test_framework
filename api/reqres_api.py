"""Модуль для работы с api https://reqres.in/"""

import allure

from api.api import Api
from model.create_model import RequestCreateUserModel
from model.login_model import (RequestLoginSuccessfulModel,
                               RequestLoginUnsuccessfulModel)
from model.register_model import (RequestRegisterSuccessfulModel,
                                  RequestRegisterUnsuccessfulModel)
from model.single_resource_model import ResponseSingleResourceModel
from model.single_user_model import ResponseSingleUserModel
from model.update_model import RequestUpdateUserModel


class ReqresApi(Api):

    """URl"""

    _URL = "https://reqres.in"

    """Endpoints"""
    _ENDPOINT_USER = "/api/users/"
    _LIST_USERS_ENDPOINT = "/api/users?page="
    _RESOURCE_ENDPOINT = "/api/unknown/"
    _LIST_RESOURCE_ENDPOINT = "/api/unknown"
    _REGISTER_ENDPOINT = "/api/register"
    _LOGIN_ENDPOINT = "/api/login"
    _DELAY_ENDPOINT = "/api/users?delay="

    @allure.step("Обращение к single user")
    def reqres_single_user(self, user_id: int):
        return self.get(url=self._URL, endpoint=self._ENDPOINT_USER + str(user_id))

    @allure.step("Обращение к create")
    def reqres_create(self, param_request_body: RequestCreateUserModel):
        return self.post(
            url=self._URL,
            endpoint=self._ENDPOINT_USER,
            json_body=param_request_body.to_dict(),
        )

    @allure.step("Обращение к update через put")
    def reqres_update_by_put(
        self, user_id: int, param_request_body: RequestUpdateUserModel
    ):
        return self.put(
            url=self._URL,
            endpoint=self._ENDPOINT_USER + str(user_id),
            json_body=param_request_body.to_dict(),
        )

    @allure.step("Обращение к update через patch")
    def reqres_update_by_patch(
        self, user_id: int, param_request_body: RequestUpdateUserModel
    ):
        return self.patch(
            url=self._URL,
            endpoint=self._ENDPOINT_USER + str(user_id),
            json_body=param_request_body.to_dict(),
        )

    @allure.step("Обращение к delete")
    def reqres_delete(self, user_id: int):
        return self.delete(url=self._URL, endpoint=self._ENDPOINT_USER + str(user_id))

    @allure.step("Обращение к list users")
    def reqres_list_users(self, page_num: int):
        return self.get(
            url=self._URL, endpoint=self._LIST_USERS_ENDPOINT + str(page_num)
        )

    @allure.step("Обращение к single resource")
    def reqres_single_resource(self, resource_id: int):
        return self.get(
            url=self._URL, endpoint=self._RESOURCE_ENDPOINT + str(resource_id)
        )

    @allure.step("Обращение к list resource")
    def reqres_list_resource(self):
        return self.get(url=self._URL, endpoint=self._LIST_RESOURCE_ENDPOINT)

    @allure.step("Обращение к register")
    def reqres_register(
        self,
        param_request_body: RequestRegisterSuccessfulModel
        or RequestRegisterUnsuccessfulModel,
    ):
        return self.post(
            url=self._URL,
            endpoint=self._REGISTER_ENDPOINT,
            json_body=param_request_body.to_dict(),
        )

    @allure.step("Обращение к login")
    def reqres_login(
        self,
        param_request_body: RequestLoginSuccessfulModel
        or RequestLoginUnsuccessfulModel,
    ):
        return self.post(
            url=self._URL,
            endpoint=self._LOGIN_ENDPOINT,
            json_body=param_request_body.to_dict(),
        )

    @allure.step("Обращение к list users с delay")
    def reqres_list_users_with_delay(self, delay: int):
        return self.get(url=self._URL, endpoint=self._DELAY_ENDPOINT + str(delay))

    """Собираем респонс в обьект для последующего использования"""

    def deserialize_single_user(self):
        """для метода get (single user)"""
        payload = self.get_payload([])
        return ResponseSingleUserModel(
            id=payload["data"]["id"],
            email=payload["data"]["email"],
            first_name=payload["data"]["first_name"],
            last_name=payload["data"]["last_name"],
            avatar=payload["data"]["avatar"],
            url=payload["support"]["url"],
            text=payload["support"]["text"],
        )

    def deserialize_single_resource(self):
        """для метода get (single resource)"""
        payload = self.get_payload([])
        return ResponseSingleResourceModel(
            id=payload["data"]["id"],
            name=payload["data"]["name"],
            year=payload["data"]["year"],
            color=payload["data"]["color"],
            pantone_value=payload["data"]["pantone_value"],
        )
