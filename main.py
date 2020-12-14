from product import Product
from category import Category

products = []
categories = []

def create_product():
  pass
def list_products():
  pass
def update_product():
  pass
def delete_product():
  pass
def find_product():
  pass
def create_category():
  pass
def list_categories():
  pass

def menu():
    options = ["Create product", "List product", "Edit product",
          "Delete product", "Find by id", "Create category",
          "List category", "Exit"]
    print("\nMENU")

    for i, option in enumerate(options):
      print(f"[{i+1}] - {option}")

    op = int(input("\nSelect option:"))
    return op

    while True:
      try:
        op = menu()
        if op == 1:
            create_product()
        elif op == 2:
            list_products()
        elif op == 3:
            update_product()  
        elif op == 4:
            delete_product()  
        elif op == 5:
            create_category()
        elif op == 6:
            list_categories()
        elif op == 7:
          exit(0) 
        else:
            print("Invalid opt!")
      except ValueError:
        print("\nOption ivalid!") 


