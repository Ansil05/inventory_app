from datetime import date
import re
class Product:
    'python oop applied'
    def __init__(self,productid=None,productname=None,unitprice=None,
                 categoryid=None,manufacturedate=None,is_active = "Y"):
        self.__productid = productid
        self.__productname = productname
        self.__unitprice = unitprice
        self.__categoryid = categoryid
        self.__manufacturedate = manufacturedate if manufacturedate else date.today()
        self.__is_active = is_active

        # if productname is not None:
        #     self.__productname = productname

    def get_productid(self):
        return self.__productid
    def set_productid(self,productid):
        self.__productid = productid
    
    def get_productname(self):
        return self.__productname
    def set_productnsme(self,productname):
        '''validation'''
        pattern = re.compile(r"^[a-zA-Z_]{2,30}$")
        while True:
            if pattern.match(productname):
                self.__productname = productname
                break
            else:
                print("invalid product name!!!!")
                productname = input("enter product name")

    def get_unitprice(self):
        return self.__unitprice
    def set_unitprice(self,unitprice):
        self.__unitprice = unitprice
    def get_categoryid(self):
        return self.__categoryid
    def set_categoryid(self,catagoryid):
        self.__categoryid = catagoryid
    def get_manufacture_date(self):
        return self.__manufacturedate
    def set_manufacture_date(self,manufactuerdate):
        if isinstance(manufactuerdate,date):
            self.__manufacturedate = manufactuerdate
        else:
            raise ValueError("amanufacture date must be date")
    def get_is_active(self):
        return self.__is_active
    def set_is_active(self,is_active):
        self.__is_active = is_active
    def __str__(self):
        return f"\nProducct Id: {self.__productid:<10}\nProduct Name: {self.__productname}\nUnit Price: {self.__unitprice}\nCategory Id: {self.__categoryid}\nManufacture date: {self.__manufacturedate}\nActive:{self.__is_active}"
    

    

