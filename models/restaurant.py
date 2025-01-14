from models.abstractclass import abstractitem
from models.foodmenu import foodmenu


class restaurant(abstractitem):
    def __init__(self,name:str,rating:int,location:str,offer):
        super().__init__(name,rating)
        self.location = location
        self.offer = offer 
        self.__foodmenu = []


    @property
    def foodmenu(self):
        return self.__foodmenu
    
    @foodmenu.setter
    def foodmenu(self,items:list):

        for item in items:
            if not isinstance(item,foodmenu):
                print("Invalid food menu")
                return 
            
        self.__foodmenu = items


    def displayitem(self,start):
        print(f"{start} Name >> {self.name} - Rating >> {self.rating}")