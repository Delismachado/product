class Product:
    __id: int
    __name: str
    __description: str    

    def __init__(self, name: str, description: str) -> None:
        self.set_id()
        self.set_name(name)
        self.set_description(description)
        

    def set_id(self) -> None:
        if len(products) == 0:
            self.__id = 1
        else:
            self.__id = products[-1].get_id() + 1

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


class Category:
    __id: int
    __name: str

    def __init__(self, name: str, ) -> None:
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

def create_product():
    print("Create a new product")
    name = input("Product name: ")
    description = input("Product description: ")    

    product = Product(name, description)
    products.append(product)
    print("Cool, registered product!")

    menu()

def find_product(id: int) -> int:
    index = -1
    for product in products:
        if product.get_id() == id:
            index = products.index(product)
            break
    
    return index

def print_product(index: int) -> None:
        print(f"ID: {products[index].get_id()}")
        print(f"Name: {products[index].get_name()}")
        print(f"Description: {products[index].get_description()}")
        

def list_products():
    if len(products) == 0:
        print("The list is empty!")
    else:
        print("Products created:")
        for product in products:
            print("id: {product.get_id()}")
            print("Name: {product.get_name()}")
            print("Description: {product.get_description()}")            

    menu()

def update_product():
    print("Update a product")
    id = int(input("Product id: "))

    index = find_product(id)

    if index >= 0:
        print("Product found!")
        print_product(index)

        name = input("New product name: ")
        description = input("New product description: ")        

        products[index].set_name(name)
        products[index].set_description(description)        

        print("Product updated!")
    else:
        print("Product not found!")

    menu()

def delete_product():
    print("Delete a product")
    id = int(input("Product id: "))

    index = find_product(id)

    if index >= 0:
        print("Product found!")
        print_product(index)
        
        opt = input("You want to delete? (Y/N) ")
        
        if opt == "Y":
            products.pop(index)
            print("Product deleted!")
    else:
        print("Product not found!")

    menu()

def menu():
    opt = -1
    while opt < 0 or opt > 4:
        print("Choose an opt:")
        print("1 - Create")
        print("2 - List")
        print("3 - Update")
        print("4 - Delete")
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
        else:
            print("Ivalid opt!")  
                

menu()