import pytest
import allure
from api.endpoints import *
from models.post import Post
from utils.payloads import Payload


@allure.feature("Posts")
class TestPosts:

    @allure.story("Получение всех постов")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_all_posts(self, api_client):
        response = get_posts(api_client)
        assert response.status_code == 200
        Post(**response.json()[0])

    @allure.story("Получение поста по ID")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("post_id", [1, 2, 3])
    def test_get_post_by_id(self, api_client, post_id):
        response = get_post_by_id(api_client, post_id)
        assert response.status_code == 200
        Post(**response.json())

    @allure.story("Получение несуществующего поста")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_non_existing_post(self, api_client):
        response = get_post_by_id(api_client, 9999)
        assert response.status_code == 404

    @allure.story("Создание поста")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_post(self, api_client):
        response = create_post(api_client, Payload.valid_post_payload())
        assert response.status_code == 201

    @allure.story("Обновление поста")
    @allure.severity(allure.severity_level.NORMAL)
    def test_update_post(self, api_client):
        response = update_post(api_client, 1, Payload.valid_put_payload())
        assert response.status_code == 200

    @allure.story("Удаление поста")
    @allure.severity(allure.severity_level.MINOR)
    def test_delete_post(self, api_client):
        response = delete_post(api_client, 1)
        assert response.status_code == 200