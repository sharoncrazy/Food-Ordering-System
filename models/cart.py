class cart :

    def __init__(self,items,choices):
        self.choices = choices
        self.fooditems = self.addtocart(items)
        

    def addtocart(self,items):
        dict = {}
        for item in self.choices:

            if choice > len(items) :
                raise KeyError
            for choice in dict:
                if choice in dict :
                    dict[choice] += 1 
                else :
                    dict[choice] = 1

        return dict
    

    # def processorder(self):
    #     for items in self.fooditems:
    #         print(f"{fooditems[items-1]} ")

