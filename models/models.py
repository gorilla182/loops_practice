from pydantic import BaseModel, Field

class ProductData(BaseModel):
    year: int
    price: float
    cpu_model: str=Field(alias='CPU model')
    hard_disk_size: str=Field(alias='Hard disk size')

    model_config = {'populate_by_name': True}

class Product(BaseModel):
    name: str
    data: ProductData

class UserData(BaseModel):
    email: str
    password: str

    model_config = {'populate_by_name': True}
