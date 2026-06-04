import pytest
import requests
from clients.api_client import ProductClient, UserClient
from test_data.test_data import macbook, user_data
from config import USERNAME_API, PASSWORD_API


@pytest.fixture
def client():
    return ProductClient()

@pytest.fixture
def create_object(client: ProductClient):
    response = client.create(macbook())
    yield response
    obj_id = response.json()['id']
    client.delete(obj_id)

@pytest.fixture
def user():
    return UserClient()

@pytest.fixture
def register_new_user(user: UserClient):
    response = user.register_new_user(user_data(USERNAME_API, PASSWORD_API))
    yield response
    obj_id = response.json()['id']
    user.delete_user(obj_id)





