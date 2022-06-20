class User:
    def __init__(self, name , last_name): #  constructor
        self.name = name
        self.last_name = last_name
    
    def printInfo(self): # method
        print( 'name: '+ self.name)
        print( 'last name: '+ self.last_name)
    
    def deleteName(self): #delete properties
        del self.name
        self.name = ''

new_user = User('Isaac', 'Grimaldo')
new_user.printInfo()
new_user.deleteName()
new_user.printInfo()