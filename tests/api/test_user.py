
import requests
import pytest
from clients.api_client import UserClient

def test_register_user(register_new_user):
    response = register_new_user.json()
    assert 'token' in response


@pytest.mark.parametrize("number_page", [2])
def test_user_data(user: UserClient, number_page):
    response = user.get_users_by_page(number_page)
    body = response.json()
    assert len(body['data']) == 6
    assert body['per_page'] == 6

