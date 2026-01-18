import pytest
import allure
from api.endpoints import *
from models.comment import Comment


@allure.feature("Comments")
class TestComments:

    @allure.story("Получение комментариев к посту")
    @allure.severity(allure.severity_level.NORMAL)
    def test_comments_by_post(self, api_client):
        response = get_comments_by_post(api_client, 1)
        assert response.status_code == 200

        for comment in response.json():
            Comment(**comment)
            assert comment["postId"] == 1