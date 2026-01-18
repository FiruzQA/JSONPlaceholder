import pytest
import sys, os
from api.client import APIClient


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")


@pytest.fixture(scope="session")
def api_client(base_url):
    return APIClient(base_url)