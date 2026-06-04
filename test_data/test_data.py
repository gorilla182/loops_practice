from models.models import Product, ProductData, UserData

def macbook() -> Product:
    return Product(
        name='Apple MacBook Pro 16',
        data=ProductData(
            cpu_model='Intel Core i9',
            hard_disk_size='1 TB',
            year=2019,
            price=1849.99
        )
    )

def user_data(username, password):
    return UserData(
        email=username,
        password=password
    )