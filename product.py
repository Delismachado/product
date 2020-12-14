class Product:
    __id: int
    __name: str
    __description: str
    __price: float
    __weight: float
    __width: float
    __height: float    
    __categories: list[str] = []      

    
    def get_id(self) -> int:
        return self.__id

    def set_id(self, id: int) -> None:
        self.__id = id


    def get_name(self) -> str:
        return self.__name    
        
    def set_name(self, name: str) -> None:
        self.__name = name
    

    def set_description(self, description: str) -> None:
        if len(description) >= 20:
            self.__description = description
        else:
            print("Try again!")

    def get_description(self) -> str:
        return self.__description



    def set_price(self, price: float) -> None:        
        self.__price = price
        

    def get_price(self) -> float:
        return self.__price


    def set_weight(self, weight: float) -> None:
        self.__weight = weight
        

    def get_weight(self) -> float:
        return self.__weight

    def set_width(self, width: float) -> None:
        self.__width = width 
      

    def get_width(self) -> float:
        return self.__width

    def set_height(self, height: float) -> None:
        self.__height = height
    
    def get_height(self) -> float:
        return self.__height

    def get_length(self) -> float:
        return self.__length

        def set_length(self, length: float) -> None:
          self.__length = length

    
    
    def get_categories(self) -> list:
        return self.__categories

    def append_categories(self, category: str) -> None:
        self.__categories.append(category)

    def __str__(self):
        return f"""
                    - ID: {self.get_id()}
                    - Name: {self.get_name()}
                    - Price: {self.get_price()}
                    - Weight: {self.get_weight()}
                    - Height: {self.get_height()}
                    - Length: {self.get_length()}
                    - Width: {self.get_width()}
                    - Description: {self.get_description()}
                 """

  
