from models.user import User_detail

class usermanager():
    __users = []

    @classmethod
    def add_users(cls,user_obj):
        if isinstance(user_obj,User_detail):
            cls.__users.append(user_obj)
            print(" You Have Sucessfully Registered")
        else :
            print("invalid User")


    @classmethod
    def check(cls,mail,pwd):
        for user in cls.__users:
            if user.Emailid == mail and user.Password == pwd :
                return user 

    