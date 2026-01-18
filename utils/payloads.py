class Payload:

    @staticmethod
    def valid_post_payload():
        return {
            "userId": 1,
            "title": "Test title",
            "body": "Test body"
        }

    @staticmethod
    def valid_put_payload():
        return {
            "userId": 1,
            "title": "Updated title",
            "body": "Updated body"
        }

    @staticmethod
    def invalid_payload():
        return {
            "userId": "invalid",
            "title": 123,
            "body": None
        }