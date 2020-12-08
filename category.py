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
    


categories = []

def create_category():
  print("Create a new category:")
  name = input("Category name:")

  category = Category(name)
  categories.append(category)


def find_category(id: int) -> int:
    idx = -1
    for category in categories:
        if category.get_id() == id:
            idx = categories.index(category)
            break
    
    return idx

def show_category(idx: int) -> None:
        print(f"Id: [categories[idx].get_id()]")
        print(f"Name: [categories[idx].get_name()]")        


def list_categories():
    if len(categories) == 0:
        print("No categories available!")
    else:
        print("Categories:")
        for category in categories:
            print("Name: {}".format(category.get_name()))
            


