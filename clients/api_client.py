import requests
from models.models import Product, UserData

class ProductClient:
    BASE_URL = 'https://api.restful-api.dev/objects'

    def create(self, product: Product):
        return requests.post(self.BASE_URL, json=product.model_dump(by_alias=True))



    def get(self, obj_id):
        return requests.get(f'{self.BASE_URL}/{obj_id}')

    def delete(self, obj_id):
        return requests.delete(f'{self.BASE_URL}/{obj_id}')

class UserClient:
    BASE_URL='https://reqres.in'
    API='reqres_cd478a4d1a7c4eebb356e988f9b3c581'
    USER_EMAIL=''
    USER_PASSWORD=''

    def register_new_user(self, user: UserData):
        return requests.post(f'{self.BASE_URL}/api/register', json=user.model_dump(), headers={'x-api-key': self.API})

    def login_user(self, user: UserData):
        return requests.post(f'{self.BASE_URL}/api/login', json=user.model_dump(), headers={'x-api-key': self.API})


    def delete_user(self, obj_id):
        return requests.delete(f'{self.BASE_URL}/{obj_id}')

    def get_users_by_page(self, number_page):
        return requests.get(f'{self.BASE_URL}/api/users', params={'page': number_page}, headers={'x-api-key': self.API})
