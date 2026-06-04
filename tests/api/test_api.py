import requests

def test_create_object(create_object):
    response = create_object.json()
    print(response)
    assert create_object.status_code == 200 #это ес че не баг а фича, данное апи на пост запрос возвращает 200, а не 201
    assert 'createdAt' in response

def test_get_object_by_id(create_object, client):
    obj_id = create_object.json()['id']
    result = client.get(obj_id)
    assert result.status_code == 200