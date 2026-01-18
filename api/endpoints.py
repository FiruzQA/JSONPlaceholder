import allure


@allure.step("Получить список постов")
def get_posts(client):
    return client.request("GET", "/posts")


@allure.step("Получить пост по ID: {post_id}")
def get_post_by_id(client, post_id):
    return client.request("GET", f"/posts/{post_id}")


@allure.step("Создать пост")
def create_post(client, data):
    return client.request("POST", "/posts", json=data)


@allure.step("Обновить пост с ID: {post_id}")
def update_post(client, post_id, data):
    return client.request("PUT", f"/posts/{post_id}", json=data)


@allure.step("Удалить пост с ID: {post_id}")
def delete_post(client, post_id):
    return client.request("DELETE", f"/posts/{post_id}")


@allure.step("Получить пользователей")
def get_users(client):
    return client.request("GET", "/users")


@allure.step("Получить пользователя по ID: {user_id}")
def get_user_by_id(client, user_id):
    return client.request("GET", f"/users/{user_id}")


@allure.step("Получить комментарии для поста {post_id}")
def get_comments_by_post(client, post_id):
    return client.request("GET", f"/posts/{post_id}/comments")