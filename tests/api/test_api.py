
import pytest
import requests

def test_create_object(create_object):
    body = create_object.json()
    assert create_object.status_code == 201
    assert 'createdAt' in body

def test_get_object_by_id(create_object):
    body = create_object.json()
    result = requests.get(f'https://api.restful-api.dev/objects/{body['id']}')
    assert result.status_code == 200