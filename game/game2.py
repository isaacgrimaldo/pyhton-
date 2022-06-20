result = 0
control = True
num1 = input('insert the number 1: ')
num2 = input('insert the number 2: ')
symbol = input('insert the operation type( + , - , x , /): ')

try: 
    num1 =  int(num1)
    num2 =  int(num2)
except:
    control = False

if control == False :
    print("ERROR DARA")
    exit()

if symbol == '+':
    result = num1 +num2
    print(result)
elif symbol == '-':
    result = num1  - num2
    print(result) 
elif symbol == '*':
    result = num1  * num2
    print(result) 
elif symbol == '/':
    result = num1  / num2
    print(result) 
else:
    print("operation not valid")
