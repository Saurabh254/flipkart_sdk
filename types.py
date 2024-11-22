from dataclasses import dataclass

@dataclass(frozen=True)
class Product:
    id: str
    name: str
    price: float
    product_description: str
