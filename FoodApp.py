from models.user import User_detail
from models.usermanager import usermanager
from controllers.mainmenu import mainmenu

class login_class:

    def login(self):
        Email = input("Enter email-id : ")
        Password = int(input("Enter a New  password : "))

        user = usermanager.check(Email,Password)
        
        if user is not None :
            print("login Sucessful")
            menu = mainmenu()
            menu.start()
        else :
            print(" Invalid Email or Password " )


    def register(self):
        Name = input("enter your name : ")
        phone_number = int(input("Enter phone number : "))
        Email = input("Enter email-id : ")
        Password = int(input("Enter a New  password : "))

        user_obj = User_detail(Name,phone_number,Email,Password)

        usermanager.add_users(user_obj)


    def guest(self):
        pass 

    def exit(self):
        pass 

    def validate_options(self,choice):
            if choice == 1 :
                self.login()

            elif choice == 2 :
                self.register()

            elif choice == 3 :
                self.guest()

            elif choice == 4 :
                print(" << Thank you for using >> ")
                exit()
                

            else :
                print("Enter a valid choice")





class FoodApp:

    Login_options = {"1":"Login", "2":"Register", "3":"Guest", "4":"Exit"}
    

    @staticmethod
    def __init__():
        print("<< welcome to sharoniggy >>")

        

        while True :
            for key in FoodApp.Login_options:
                print(f"{key}.{FoodApp.Login_options[key]}",end="  ")
            print()
            login_class_obj = login_class()

            
            choice = int(input("Enter your choice :"))
            login_class_obj.validate_options(choice)

    # menu = mainmenu()
    # menu.start()

        
            

            