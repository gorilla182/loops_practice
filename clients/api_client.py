import requests
from models.models import Product

class ProductClient:
    BASE_URL = 'https://api.restful-api.dev/objects'

    def create(self, product: Product):
        return requests.post(self.BASE_URL, json=product.model_dump(by_alias=True))



    def get(self, obj_id):
        return requests.get(f'{self.BASE_URL}/{obj_id}')

    def delete(self, obj_id):
        return requests.delete(f'{self.BASE_URL}/{obj_id}')
