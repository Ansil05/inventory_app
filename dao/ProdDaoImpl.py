from dao.AbsProdDao import ProductDaoService
from db.db_connection import DBConnection
from typing import List
from models.product import Product

class ProductDaoImplentation(ProductDaoService):
    DISPLAY_ALL = "SELECT * FROM products"
    INSERT_PRODUCT = "INSERT INTO products(productname,unitprice,categoryid,manufacturedate,isactive) VALUES (%s,%s,%s,%s,%s)"
    FIND_BY_ID = "SELECT * FROM products WHERE productid = %s"
    UPDATE_PRODUCT = "UPDATE products SET productname = %s,unitprice = %s WHERE productid = %s"
    FIND_BY_NAME = "SELECT * FROM products WHERE productname = %s"
    DISABLE_PRODUCT = "UPDATE products SET isactive = %s WHERE productname = %s"
    APPLY_GST = "CALL apply_gst_to_product(%s,%s)"
    def __init__(self):
        self.conn = DBConnection().get_connection()
    def insert_product(self,product:Product)->bool:
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.INSERT_PRODUCT,(product.get_productname(),product.get_unitprice(),product.get_categoryid(),product.get_manufacture_date(),product
                                                .get_is_active()))
            self.conn.commit()
            return cursor.rowcount == 1
        except Exception as e:
            print("Error inserting product:",e)
            return False
        finally:
            cursor.close()
    def display_all_product(self)->List[Product]:
        Products = []
        try:
            cursor = self.conn.cursor(dictionary = True)
            cursor.execute(self.DISPLAY_ALL)
            rows = cursor.fetchall()
            for row in rows:
                Products.append(Product(productid = row["productid"],
                                        productname = row["productname"],
                                        unitprice = row["unitprice"],
                                        categoryid = row["categoryid"],
                                        manufacturedate = row["manufacturedate"],
                                        is_active = row["isactive"]))
        except Exception as e:
            print("Error fetching products:",e)    
        finally:
            cursor.close()
        return Products    
    def find_by_product_id(self, productid):
        product = None
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(self.FIND_BY_ID,(productid,))
            row = cursor.fetchone()
            if row:
                product = Product(productid = row["productid"],
                                        productname = row["productname"],
                                        unitprice = row["unitprice"],
                                        categoryid = row["categoryid"],
                                        manufacturedate = row["manufacturedate"],
                                        is_active = row["isactive"])
        except Exception as e:
            print("error occured when fetching:",e)
        finally:
            cursor.close()
        return product
    def update_product(self, product:Product, productid:int):
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.UPDATE_PRODUCT,(product.get_productname(),product.get_unitprice(),productid))
            self.conn.commit()
            return cursor.rowcount == 1
        except Exception as e:
            print("error when updating the product:",e)
            return False
        finally:
            cursor.close()
    def find_by_product_name(self, productname):
        product = None
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(self.FIND_BY_NAME,(productname,))
            row = cursor.fetchone()
            if row:
                product = Product(productid = row["productid"],
                                        productname = row["productname"],
                                        unitprice = row["unitprice"],
                                        categoryid = row["categoryid"],
                                        manufacturedate = row["manufacturedate"],
                                        is_active = row["isactive"])
        except Exception as e:
            print("error occured when fetching:",e)
        finally:
            cursor.close()
        return product
    def disable_product(self,productname:str):
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.DISABLE_PRODUCT,("N",productname))
            self.conn.commit()
            return cursor.rowcount == 1
        except Exception as e:
            print("error when updating the product:",e)
            return False
        finally:
            cursor.close()
    def apply_gst(self, product_id:int,gst_percent:float):
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.APPLY_GST,(product_id,gst_percent))
            self.conn.commit()
            return cursor.rowcount >=0
        except Exception as e:
            print("Error Applying GST:",e)
            return False
        finally:
            cursor.close()
        


        
