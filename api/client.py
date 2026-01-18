import requests
import allure
from utils.logger import logger


class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def request(self, method: str, endpoint: str, json=None):
        url = self.base_url + endpoint
        logger.info(f"{method} {url}")

        with allure.step(f"{method} {endpoint}"):
            # attach request
            allure.attach(
                body=str({
                    "method": method,
                    "url": url,
                    "payload": json
                }),
                name="Request",
                attachment_type=allure.attachment_type.JSON
            )

            response = requests.request(
                method=method,
                url=url,
                json=json,
            )

            # attach response
            allure.attach(
                body=response.text,
                name=f"Response [{response.status_code}]",
                attachment_type=allure.attachment_type.JSON
            )

            return response