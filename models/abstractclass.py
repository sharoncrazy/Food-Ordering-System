from abc import ABC , abstractmethod

class abstractitem(ABC):

    def __init__(self,name,rating = None):
        self.name = name
        self.rating =  rating

    @abstractmethod
    def displayitem(self,start):
        pass