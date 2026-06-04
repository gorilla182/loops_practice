import pytest
import requests

@pytest.fixture
def create_object():
    product = {
  "name": "Apple MacBook Pro 16",
  "data": {
    "year": 2019,
    "price": 1849.99,
    "CPU model": "Intel Core i9",
    "Hard disk size": "1 TB"
  }
}
    response = requests.post('https://api.restful-api.dev/objects', json=product)
    yield response
    body = response.json()
    requests.delete(f'https://api.restful-api.dev/objects/{body['id']}')



