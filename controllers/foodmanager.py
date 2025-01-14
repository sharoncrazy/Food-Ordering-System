from models.fooditem import fooditem
from models.restaurant import restaurant
from models.foodmenu import foodmenu


class foodmanager():

    def __init__(self):
        self.restaurants = self.__preparerestaurant()


    def __preparefooditems(self):
        item1 = fooditem("Fried Chicken",4.7,240,"Indian")
        item2 = fooditem("Chicken Roll",4.9,120,"Indian")
        item3 = fooditem("Pizza",4.2,360,"American")
        item4 = fooditem("Smilies",4.3,200,"Italian")
        item5 = fooditem("Tacos",4.5,110,"Chineese")
        return[item1,item2,item3,item4,item5]

    def __preparefoodmenu(self):
        foodItems = self.__preparefooditems()
        menu1 = foodmenu("Veg")
        menu1.fooditems = [foodItems[1],foodItems[3]]
        menu2 = foodmenu("Non veg")
        menu2.fooditems = [foodItems[0],foodItems[2],foodItems[4]]
        menu3 = foodmenu("Continental")
        menu3.fooditems = [foodItems[2],foodItems[3],foodItems[4]]
        return [menu1,menu2,menu3]

    def __preparerestaurant(self):
        foodMenus = self.__preparefoodmenu()
        res1 = restaurant("Burger King",4.6,"Anna nagar",10)
        res1.foodmenu = [foodMenus[0],foodMenus[1],foodMenus[2]]

        res2 = restaurant("Subway",4.8,"K.K Nagar",20)
        res2.foodmenu = [foodMenus[1],foodMenus[2]]

        res3 = restaurant("KFC",3.9,"Iyer banglow",8)
        res3.foodmenu = [foodMenus[0],foodMenus[1]]

        res4 = restaurant("Taco Bell",4.9,"ByPass Road",20)
        res4.foodmenu = [foodMenus[0]]

        return [res1,res2,res3,res4]
    
    def findrestaurant(self,name):
        for res in self.restaurants:
            if res.name == name:
                return res 
            
    def findfooditem(self):
        pass

        
