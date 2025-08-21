from abc import ABC,abstractmethod
from typing import List
from models.product import Product

class ProductDaoService(ABC):
    @abstractmethod
    def insert_product(self)->bool:
        pass
    @abstractmethod
    def display_all_product(self)->List[Product]:
        pass
    @abstractmethod
    def find_by_product_id(self,productid:int)->Product:
        pass
    @abstractmethod
    def find_by_product_name(self,productname:str)->Product:
        pass
    @abstractmethod
    def update_product(self,product:Product,productid:int)->bool:
        pass
    @abstractmethod
    def disable_product(self,productname:str)->bool:
        pass
    @abstractmethod
    def apply_gst(self,product_id:int,gst_percent:float)->bool:
        pass


