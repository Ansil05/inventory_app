from dao.ProdDaoImpl import ProductDaoImplentation
from dao.AbsProdDao import ProductDaoService
from models.product import Product
from datetime import datetime, date
class ProductManagementLib:
    dao_service: ProductDaoService = ProductDaoImplentation()
    @staticmethod
    def display_all():
        products = ProductManagementLib.dao_service.display_all_product()
        for product in products:
            print(product)
    @staticmethod
    def add_product():
        product = Product()
        productname = input("Enter the product Name: ")
        product.set_productnsme(productname)
        unitprice = float(input("Enter the unit price: "))
        product.set_unitprice(unitprice)
        categoryid = int(input("Enter the category id"))
        product.set_categoryid(categoryid)
        m_date = input("enter the manufacturing date(DD/MM/YYYY):") or date.today()
        if isinstance(m_date,str):
            util_date = datetime.strptime(m_date,"%d/%m/%Y")
            conv_m_date = util_date.date()
        else:
            conv_m_date = m_date
        product.set_manufacture_date(conv_m_date)
        product.set_is_active("Y")

        if ProductManagementLib.dao_service.insert_product(product):
            print("successfully added...")
        else:
            print("not done yet")
    @staticmethod
    def update_product():
        searchid = int(input("Enter the product id: "))
        product = ProductManagementLib.dao_service.find_by_product_id(searchid)
        if not product:
            print("No product found!!!")
            return
        print(product)
        conform = input("do you want to update(y/n): ")
        if conform.strip().lower() == "y":
            product.set_productnsme(input("Enter the new name: "))
            product.set_unitprice(input("Enter the unit price: ")) 
            if ProductManagementLib.dao_service.update_product(product,searchid):
                print("successfully updated")
            else:
                print("something went wrong!!! ")
    def disable_product():
        searchname = input("Enter the name to search:")
        product = ProductManagementLib.dao_service.find_by_product_name(searchname)
        if not product:
            print("No product found!!!")
            return
        print(product)
        conform = input("do you want to DISABLE(y/n): ")
        if conform.strip().lower() == "y":
            if ProductManagementLib.dao_service.disable_product(searchname):
                print("successfully disabled")
            else:
                print("something went wrong!!! ")
    @staticmethod
    def apply_gst():
        product_id = int(input("Enter the product id: "))
        gst_percentage = float(input("Enter the GST percentage to apply:"))
        if ProductManagementLib.dao_service.apply_gst(product_id,gst_percentage):
            print("")





        



