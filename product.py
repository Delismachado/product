class Product:
    __id: int
    __name: str
    __description: str
    __price: float
    __weight: float
    __width: float
    __height: float    
    __categories: list[str] = []


    def __init__(self, name: str, description: str, price: float, weight: float, width: float, height: float, categories: list[str]) -> None:        
        self.set_id()
        self.set_name(name)
        self.set_description(description)
        self.set_price(price)
        self.set_weight(weight)
        self.set_width(width)
        self.set_height(height)        
        self.set_categories(categories)
        

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
        if len(description) <= 20:
            self.__description = description
        else:
            raise ValueError("To long!") 

    def get_description(self) -> str:
        return self.__description

    def set_price(self, price: float) -> None:
        if price > 0:
            self.__price = price
        else:
            raise ValueError("Price must be positive!")

    def get_price(self) -> float:
        return self.__price

    def set_weight(self, weight: float) -> None:
        if weight > 0:
            self.__weight = weight
        else:
            raise ValueError("Weight must be positive!")

    def get_weight(self) -> float:
        return self.__weight

    def set_width(self, width: float) -> None:
        if width> 0:
            self.__width = width
        else:
            raise ValueError("Width must be positive!")

    def get_width(self) -> float:
        return self.__width

    def set_height(self, height: float) -> None:
        if height > 0:
            self.__height = height
        else:
            raise ValueError("Height must be positive!")

    def get_height(self) -> float:
        return self.__height

    def set_categories(self, categories: list[str]) -> None:
        self.__categories = categories

    def append_category(self, category: str) -> None:
        self.__categories.append(categories)

    def get_categories(self) -> str:
        return self.__categories

    def print_product(self) -> None:
            print(f"Id: {self.get_id()}")
            print(f"Name: {self.get_name()}")
            print(f"Description: {self.get_description()}")
            print(f"Price: R${self.get_price()}")
            print(f"Weight: {self.get_weight()} kg")
            print(f"Width: {self.get_width()} m")
            print(f"Height: {self.get_height()} m")            
            print(f"Categories: {self.get_categories()}\n")

        
class Category:
    __id: int
    __name: str

    def __init__(self, name: str) -> None:
        self.set_id()
        self.set_name(name)

    def set_id(self) -> None:
        if len(categories) == 0:
            self.__id = 1
        else:
            self.__id = categories[-1].get_id() + 1

    def get_id(self) -> int:
        return self.__id

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name       

products = []
categories = []
categories.append(Category('Category 1'))
categories.append(Category('Category 2'))
categories.append(Category('Category 3'))

def create_product():
    print("Create a new product")
    name = input("Product name: ")
    description = input("Product description: ")
    price = float(input("Product price: "))
    weight = float(input("Product weight: "))
    width = float(input("Product width: "))
    height = float(input("Product height: "))
    
    prod_categories = []

    exit_menu = False
    while not exit_menu:
        list_categories()
        chosen_id = int(input("Choose a category (id):"))

        if chosen_id == 0 :
            exit_menu = True
        else :
            category_idx = find_category_index(chosen_id)
            if category_idx == -1:
                print("Category not found!")
            else:
                chosen_category = categories[category_idx]
                already_added = False
                for cat in prod_categories:
                    if cat == chosen_category.get_name():
                        already_added = True
                    print("em construção!")
                    
                
                prod_categories.append(chosen_category.get_name())

    product = Product(name, description, price, weight, width, height, prod_categories)

    products.append(product)
    print("Product created!")

def create_category():
    print("Create a new category:")
    name = input("Category name:")

    category = Category(name)
    categories.append(category)


def find_category_index(id: int) -> int:
    idx = -1
    for category in categories:
        if category.get_id() == id:
            idx = products.index(category)
            break
    return idx

def find_product(id: int) -> int:
    idx = -1
    for product in products:
        if product.get_id() == id:
            idx = products.index(product)
            break
    return idx

def list_categories():
    if len(categories) == 0:
        print("No categories available!")
    else:
        print("Categories:")
        for category in categories:
            print("{} - Name: {}".format(category.get_id(), category.get_name()))

def list_products():
    if len(products) == 0:
        print("The list is empty!")
    else:
        print("Products created:")
        for product in products:            
            product.print_product()

def update_product():
    print("Update a product")
    id = int(input("Product id: "))

    idx = find_product(id)

    if idx >= 0:
        print("Product found!")
        products[idx].print_product()

        name = input("New product name: ")
        description = input("New product description: ")
        price  = float(input("New product price R$: "))
        weight = float(input("New product weight kg: "))
        width  = float(input("New product width m: "))
        height = float(input("New product height m: "))              

        products[idx].set_name(name)
        products[idx].set_description(description)
        products[idx].set_price(price)
        products[idx].set_weight(weight) 
        products[idx].set_width(width)
        products[idx].set_weight(weight)
        products[idx].set_height(height)       

        print("Product updated!")
    else:
        print("Product not found!")

def delete_product():
    print("Delete a product")
    id = int(input("Product id: "))

    idx = find_product(id)

    if idx >= 0:
        print("Product found!")
        products[idx].print_product()
        
        opt = input("You want to delete? (Y/N) ")
        
        if opt == "Y":
            del products[idx]
            print("Product deleted!")
    else:
        print("Product not found!")

def menu():
    opt = -1
    exit_menu = False
    while not exit_menu:
        print("Hi! choose an opt or 0 for exit")
        print("1 - Create")
        print("2 - List")
        print("3 - Update")
        print("4 - Delete")
        print("5 - Create category")
        print("6 - List category")      
        print("0 - Exit")
        
        opt = int(input("opt: "))

        if opt == 0:
            exit_menu = True
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
            print("Invalid opt!") 

    return opt
                
menu()
