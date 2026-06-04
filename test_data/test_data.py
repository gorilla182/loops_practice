from models.models import Product, ProductData

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