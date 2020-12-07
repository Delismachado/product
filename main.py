class Product:
    __name: str
    __description: str
    

    def __init__(self, name, description):
        try:
            self.set_name(name)
            self.set_description(description)

        except:
            print("Error")

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_description(self) -> str:
        return self.__description

    def set_description(self, description: str):
        self.__description = description    


def create_product():
    try:
        name = input("Product's name:")
        description = input("Product description:")        
        prod['Products'].append(Product(name, description))        
    except TypeError:
        print("Try again")        


def list_products():
    for i, e in enumerate(prod["Products"]):        
        print("[%d] %d" % (i,e))

def update_product():
    try:
        input = input("Enter product id:")             

    except:
        print("Error")       


def delete_product():
  pass #todo

def menu():
    print("Choice:")
    print("1 - create")
    print("2 - list")
    print("3 - update")
    print("4 - delete")
    print("0 - Quit")

    input_str = input()
    while input_str not in ["0", "1", "2", "3", "4"]:
        print("Choose a valid option.")
        print("1 - create")
        print("2 - list")
        print("3 - update")
        print("4 - delete")
        input_str = input_str()

    if input_str == "1":
        create_product()
        menu()
    elif input_str == "2":
        list_products()
        menu()
    elif input_str == "3":        
        update_product()
        menu()
    elif input_str == "4":        
        delete_product()
        menu()
    elif input_str == "0":
        exit()


prod = {
    "Products": []
}
menu()  