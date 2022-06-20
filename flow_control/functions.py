def myFunction():
    print("first function")

myFunction()

def functionWithArgs(arg):
    print('mi param is: ', arg)

functionWithArgs(50)

def functionWithArgUndefine(*args): # created a new tupla 
    print(args)
    

functionWithArgUndefine('isaax', 'dsadsa', 8121,1231)

def functionWithDictionaryArgs(**dictionary): # created a dictionary
    print(dictionary)

functionWithDictionaryArgs(name='isaac', last_name ='dsadasd')

def functionReturnSomething(data):
    for i in data:
        print(i)

    return data[len(data) - 1]

last_index = functionReturnSomething(['isaac','dog','table'])
print('in the last index the it is: ', last_index)