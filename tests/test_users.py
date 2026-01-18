import pytest
import allure
from api.endpoints import *
from models.user import User


@allure.feature("Users")
class TestUsers:

    @allure.story("Получение всех пользователей")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_users(self, api_client):
        response = get_users(api_client)
        assert response.status_code == 200
        assert len(response.json()) == 10

    @allure.story("Получение пользователя по ID")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_user_by_id(self, api_client):
        response = get_user_by_id(api_client, 1)
        assert response.status_code == 200
        User(**response.json())