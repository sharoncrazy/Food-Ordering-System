from models.abstractclass import abstractitem

class fooditem(abstractitem):

    def __init__(self,name:str,rating:int,price:int,description):
        super().__init__(name,rating)
        self.price = price
        self.description = description


    def displayitem(self,start):
        print(f"{start}  {self.name} price : {self.price}")
