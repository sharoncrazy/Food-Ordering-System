from models.abstractclass import abstractitem
from models.fooditem import fooditem

class foodmenu(abstractitem):

    def __init__(self,name):
        super().__init__(name)
        self.__fooditem = []

    @property
    def fooditems(self):
        return self.__fooditem
    
    @fooditems.setter
    def fooditems(self,items:list):
        for item in items:
            if not isinstance(item,fooditem):
                print("Invalid food item")
                return 
            
        self.__fooditem = items

    def displayitem(self,start):
        print(f"{start} name => {self.name}")

