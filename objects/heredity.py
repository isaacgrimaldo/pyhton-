class Human:
    def __init__(self, name , last_name):
        self.name = name
        self.last_name = last_name
        self.role ='none'

class User(Human):
    def __init__(self, name, last_name):
        super().__init__(name, last_name)
        self.role = 'user'

class Admin(Human):
    def __init__(self, name, last_name):
        super().__init__(name, last_name)
        self.role = 'admin'

new_admin =  Admin('Isaac', 'Grimaldo')
new_user = User('Damian', 'Moreno') 

print(new_admin.role)
print(new_user.role)