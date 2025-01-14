from controllers.foodmanager import foodmanager
from models.cart import cart

    


class mainmenu():
    

    __options = {1 : "Show Restaurants" , 2 : "Show Fooditems", 3 : "search restaurant", 4 : "Search Fooditem", 5 : "Logout"}

    def __init__(self):
        self.__foodmanager = foodmanager()

    def ShowRestaurants(self):
        for i,res in enumerate(self.__foodmanager.restaurants,1):
            res.displayitem(i)

        choice = int(input("select a restraunt"))
        res = self.__foodmanager.restaurants[choice]

        self.showmenu(res.foodmenu)
            

    def showmenu(self,menus):
        print("\n\n list of menus available")
        for i,menu in enumerate(menus,1):
            menu.displayitem(i)

        choice = int(input("please choose menu :  "))
        fooditems = menus[choice-1].fooditems
        self.ShowFooditems(fooditems)

        

    def __str__(self):
            return f"{self.name} - Rating: {self.rating}"
        





            

    def ShowFooditems(self,fooditems=None):
        print("showing food item from all restraunts >> ")
        if foodmanager is not None:
            for i, fooditems in enumerate(fooditems,1):
                fooditems.displayitem(i)
            
            print("choices")

            choices = list(map(int,input("please choose your fooditem").split(',')))
            # cart = cart(fooditems,choices)
            # cart.processorder()
        else :
            pass

    def searchrestaurant(self):
        res_name = input("enter a restaurant name")
        res = self.__foodmanager.findrestaurant(res_name)

        if res is not None:
            print("Restaurant Found")
            print(f"Name : {res.name }, rating {res.rating}")

        else :
            print(f"Cannot find the restraunt :  {res_name}")

    def SearchFooditem(self): # do it on your own
        pass

    def Logout(self):
        exit()

    def validate_menu(self,value):

        if value == 1:
            self.ShowRestaurants()

        if value == 2 :
            self.ShowFooditems()

        if value == 3 :
            self.searchrestaurant()

        if value == 5 :
            self.Logout()



    def start(self):

        while True : 
            for option in mainmenu.__options:
                print(f"{option}.{mainmenu.__options[option]}",end="  ")
            print()

            
            value = int(input("Enter your choice :"))
            self.validate_menu(value)





            
        