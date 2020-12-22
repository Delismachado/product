from product import Product
from category import Category

products = []
categories = []

def valid_number(number: float) -> float:
    try:
        while float(number) <= 0:
            number = float(input('try something greater than 0 '))
    except ValueError:
        number = valid_number(input('Need to be a number: '))
    return number

def new_category():
    print('\nCreate category')
    
    category = Category()
    
    category.set_name(input("Category name: "))
    if not categories:
        category.set_id(1)
        categories.append(category)
    else:
        new_id = categories[-1].get_id() + 1
        category.set_id(new_id)
        categories.append(category)
    print("successfully!")

def list_categories():
    print('\nCategories: ')
    
    for c in categories:
        print(c)
    
def new_product() -> None:
    print('Create product')
    
    product = Product()
    sku_not_valid = True
    sku = ""
    while sku_not_valid:
        sku = input('Product SKU: ')
        p = search_product(sku)
        if not p:
            sku_not_valid = False
            break
        print('SKU invalid, try again')
    
    product.set_sku(sku)
    name = input('Product name: ')
    product.set_name(name)
    price = input('Product price: ')
    product.set_price(valid_number(price))
    weight = input('Product weight: ')
    product.set_weight(valid_number(weight))
    height = input('Product height: ')
    product.set_height(valid_number(height))
    length = input('Product length: ')
    product.set_length(valid_number(length))
    width = input('Product width: ')
    product.set_width(valid_number(width))
    description = input('Product description: ')
    product.set_description(description)

    products.append(product)


def list_products():
    if len(products) > 0:
        print('\nList products')
        for product in products:
            print(product)
    else:
        print('\nNo products available.')


def input_sku():
    initial_product = input('Product SKU: ')
    return search_product(initial_product)


def search_product(sku: str) -> Product:
    for product in products:
        if product.get_sku() == sku:
            return product


def product_detail():
    p = input_sku()
    if not p:
        print('Product not found.')
    else:
        print(p)


def delete_product():
    p = input_sku()
    if not p:
        print('Product not found.')
    else:
        products.remove(p)
        print('Product deleted successfully')


def edit_product():
    p = input_sku()
    if not p:
        print('Product not found.')
    else:
        print(p)
        
        name = input('Product name: ')
        p.set_name(name)
        price = input('Product price: ')
        p.set_price(valid_number(price))
        weight = input('Product weight: ')
        p.set_weight(valid_number(weight))
        height = input('Product height: ')
        p.set_height(valid_number(height))
        length = input('Product length: ')
        p.set_length(valid_number(length))
        width = input('Product width: ')
        p.set_width(valid_number(width))
        description = input('Product description: ')
        p.set_description(description)


def menu():
    options = ['Create product', 'Edit Product', 'List Product', 
               'Find Product by SKU', 'Delete Product', 'Create Category', 
               'List Categories', 'Exit']

    print('\nMENU: ')

    for i, option in enumerate(options):
        print(f'[{i+1}] - {option}')

    op = int(input('Select one option: '))
    return op


while True:
    try:
        op = menu()
        if op == 1:
            new_product()
        elif op == 2:
            edit_product()
        elif op == 3:
            list_products()
        elif op == 4:
            product_detail()
        elif op == 5:
            delete_product()
        elif op == 6:
            new_category()
        elif op == 7:
            list_categories()
        elif op == 0:
            exit(0)
        else:
            print('Option unavailable.')
    except ValueError:
        print('Option unavailable.')
menu()