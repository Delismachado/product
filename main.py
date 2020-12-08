class Product:
    __id: int
    __name: str
    __description: str
    __categories: list[str]


    def __init__(self, name: str, description: str, categories: []) -> None:
        self.set_id()
        self.set_name(name)
        self.set_description(description)
        self.set_categories([])
        

    def set_id(self) -> None:
        self.__id = id        

    def get_id(self) -> int:
        return self.__id
        
    def set_name(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_description(self, description: str) -> None:
        self.__description = description

    def get_description(self) -> str:
        return self.__description

    def set_categories(self, categories: list[str]) -> None:
        self.__categories = categories

    def get_categories(self) -> list[str]:
        return self.__categories


class Category:
    __id: int
    __name: str

    def __init__(self, name: str) -> None:
        self.set_id()
        self.set_name(name)

    def set_id(self) -> None:
        self.__id = id

    def get_id(self) -> int:
        return self.__id
        
    def set_name(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name       

products = []
categories = []


def create_category():
    print("Create a new category:")
    name = input("Category name:")

    category = Category(name)
    categories.append(category)

    menu()

   


def list_categories():
    if len(categories) == 0:
        print("No categories available!")
    else:
        print("Categories:")
        for category in categories:
            print("Name: {}".format(category.get_name()))
            
    menu()

def create_product():
    print("Create a new product")
    name = input("Product name: ")
    description = input("Product description: ")

    print("Choose category:")

    prod_categories = []
    opr = 1
    while opr != 0:
        if len(categories) == 0:
            print("No categories available!")
        else:
            print("Categories:")
            for category in categories:
                print("{}. Name: {}".format([category.get_id(), category.get_name()]))
        opr = int(input("Choose the category id: "))
        # buscar categoria com o id escolhido
        
        # adicionar nome da categoria em prod_categories
        print(opr)

    product = Product(name, description, prod_categories)
    products.append(product)
    print("Cool, registered product!")

    menu()    


def find_product(id: int) -> int:
    idx = -1
    for product in products:
        if product.get_id() == id:
            idx = products.index(product)
            break
    
    return idx

def show_product(idx: int) -> None:
        print(f"Id: [products[idx].get_id()]")
        print(f"Name: [products[idx].get_name()]")
        print(f"Description: {products[idx].get_description()}")
        print(f"Category: {products[idx].get_category()}")
        

def list_products():
    if len(products) == 0:
        print("The list is empty!")
    else:
        print("Products created:")
        for product in products:
            print("Id: {}".format(product.get_description()))
            print("Name: {}".format(product.get_name()))
            print("Description: {}".format(product.get_description()))
            print("Category: {}".format(product.get_categories()))            

    menu()

def update_product():
    print("Update a product")
    id = int(input("Product id: "))

    idx = find_product(id)

    if idx >= 0:
        print("Product found!")
        show_product(idx)

        name = input("New product name: ")
        description = input("New product description: ")        

        products[idx].set_name(name)
        products[idx].set_description(description)        

        print("Product updated!")
    else:
        print("Product not found!")

    menu()

def delete_product():
    print("Delete a product")
    id = int(input("Product id: "))

    idx = find_product(id)

    if idx >= 0:
        print("Product found!")
        show_product(idx)
        
        opt = input("You want to delete? (Y/N) ")
        
        if opt == "Y":
            del products[idx]
            print("Product deleted!")
    else:
        print("Product not found!")

    menu()

def menu():
    opt = -1
    while opt < 0 or opt > 7:
        print("Hi! choose an opt or 0 for exit")
        print("1 - Create")
        print("2 - List")
        print("3 - Update")
        print("4 - Delete")
        print("6 - Create category")
        print("5 - List category")        
        print("7 - choose category")
        print("0 - Exit")
        
        opt = int(input("opt: "))

        if opt == 0:
            break
        elif opt == 1:
            create_product()
        elif opt == 2:
            list_products()
        elif opt == 3:
            update_product()            
        elif opt == 4:
            delete_product()        
        elif opt == 5:
            create_category()
        elif opt == 6:
            list_categories()        
        else:
            print("Ivalid opt!")  
                

menu()