from flask_login import UserMixin

  
# class Role():
#     id = 0
#     title = ""
    
#     def __init__(self, id, title):
#         self.id = id
#         self.title = title

# class Services():
#     service_type = ""
    
# class Payments():
#     payment_type = ""
    
# class Credentials():
#     id = 0;
#     login = ""
#     password = ""
#     u_id = 0
    
#     def __init__(self, id = 0, login = "", password = "", u_id = 0):
#         self.id = u_id
#         self.login = login
#         self.password = password
#         self.u_id = u_id
        
# class User(UserMixin):
#     id = 0
#     name = ""
#     surname = ""
#     lastname = ""
    
#     def __init__(self, id = 0, name = "", surname = "", lastname = ""):
#         self.id = id
#         self.name = name
#         self.surname = surname
#         self.lastname = lastname
        
#     def get_id(self):
#         return self.id
        
class Credentials():
        def _init_(self, cred_id, login, password, user_id):
            self.id = cred_id
            self.login = login
            self.password = password
            self.user_id = user_id
            