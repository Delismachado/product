
class Store:  
    self.products = []

    def add_product(self, product):
        product.store = self
        self.products.append(product)   

    def delete_product(self, index):
      print('No product available') if len(self.products) == 0 else self.products.remove(self.products[index])
    
    def list_product(self):
       product = [print(product) for product in self.products]
       return product
    
    def update_product(self, old_product, new_product):
       for i in self.products:
        if i == old_product: old_product = new_product
        else: print('Error')        
