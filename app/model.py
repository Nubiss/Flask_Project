class Role():
    id = 0
    title = ""
    
    def __init__(self, id, title):
        self.id = id
        self.title = title

class Users():
    name = ""
    surname = ""
    
class Services():
    service_type = ""
    
class Payments():
    payment_type = ""
    
class Credentials():
    id = 0;
    login = ""
    password = ""
    u_id = 0
    
    def _init_(self, id = 0, login = "", password = "", u_id = 0):
        self.id = u_id
        self.login = login
        self.password = password
        self.u_id = u_id
        