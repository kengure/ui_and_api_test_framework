"""Фикстуры"""
import pytest
from selenium import webdriver

from api.reqres_api import ReqresApi


@pytest.fixture(scope="function")
def reqres_api() -> ReqresApi:
    """Коннект к api reqres"""
    return ReqresApi()


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="c:/chromedriver.exe")
    yield driver
    driver.quit()
