from LIB.ProdManagLib import ProductManagementLib
def main():

    while True:
        print("\n==============product management menu=================")
        print("1.add product")
        print("2.display products")
        print("3.update product")
        print("4.search products by id")
        print("5.disable product")
        print("6.exit")
        choice = int(input("enter your choice"))
        if choice == 1:
            ProductManagementLib.add_product()
        elif choice == 2:
            ProductManagementLib.display_all()
        elif choice == 3:
            ProductManagementLib.update_product()
        elif choice == 4:
            ProductManagementLib.search_product()
        elif choice == 5:
            ProductManagementLib.disable_product()
        elif choice == 6:
            break

if __name__ == "__main__":
    main()