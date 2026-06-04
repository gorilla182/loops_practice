import pytest
import requests
from clients.api_client import ProductClient
from test_data.test_data import macbook


@pytest.fixture
def client():
    return ProductClient()

@pytest.fixture
def create_object(client: ProductClient):
    response = client.create(macbook())
    yield response
    obj_id = response.json()['id']
    client.delete(obj_id)


