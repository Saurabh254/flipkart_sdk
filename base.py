from abc import ABCMeta

from flipkart_sdk.types import Product


class BaseRepository(metaclass=ABCMeta):
    def get_product_list(self, product_name: str) -> list[Product]:
        raise NotImplementedError("Get Product list not implemented")

    def get_product_by_id(self, product_id: str) -> Product:
        raise NotImplementedError("Get Product by id not implemented")
    
    def get_product_by_name(self, product_name: str) -> Product:
        raise NotImplementedError("Get Product by name not implemented")
