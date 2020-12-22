class Category:
    __id: int
    __name: str
    __id_parent: int 

    def set_id(self, id: int) -> None:
        self.__id = int(id)

    def get_id(self) -> int:
        return self.__id

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_id_parent(self, id_parent: int) -> None:
        self.__id_parent = id_parent

    def get_id_parent(self) -> int:
        return self.__id_parent

    def __str__(self):
        return f"""
                Id: {self.get_id()}
                Name: {self.get_name()}
                Id Parent: 
                """