from decimal import Decimal
from typing import List

from products.models import Product
from products.repositories.products import ProductRepository

class ProductService:
    
    # #se puede utilizar con el init, y se necesita pasar siempre el self:
    
    # def __init__(self, prodcut_repository: ProductRepository):
    #     self.product_repository = prodcut_repository
    
    # def get_all(self) -> list[Product]:
    #     return self.product_repository.get_all()
    
    staticmethod
    def create(
        name:str,
        price:float,
        descriotion: str,
        stock:int,
    ) -> Product:
        return ProductRepository.create(
            name=name, 
            price=price, 
            description=descriotion,
            stock=stock,
    )
    
    @staticmethod
    def delete(product_id) -> bool:
        product = ProductRepository.get_by_id(product_id)
        if product:
            return ProductRepository.delete(product=product)
        return False
    
    @staticmethod
    def update(
        product_id:int,
        price:float,
        descritpion:str,
        stock:int,
    ) -> bool:
        product = ProductRepository.get_by_id(product_id)
        if product:
            ProductRepository.update(
                product=product, 
                price=price, 
                description=descritpion,
                stock=stock,
            )
            
    @staticmethod
    def get_all() -> list[Product]:
        return ProductRepository.get_all()
    
    @staticmethod
    def get_by_id(product_id:int) -> Product:
        return ProductRepository.get_by_id(product_id)
    
    @staticmethod
    def search_by_name(name:str) -> list[Product]:
        return ProductRepository.search_by_name(name)
    
    staticmethod
    def filter_by_price(
        min_price:float,
        max_price:float,
    ) -> list[Product]:
        return ProductRepository.filter_by_price(min_price, max_price)
    
    @staticmethod
    def sum_total_price(product_list: List[Product]) -> Decimal:
        total = Decimal(0)
        for product in product_list:
            total += product.price
        return total
            
#?agregar todos lo métodos de la clase ProductRepository OK!


            

