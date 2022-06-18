# simples ifs
if 2 > 5 :
    print("it's false")

if 10 < -5 :
    print("it's true")

if 1 != 5:
    print("it's true")

if 45 >= 45 :
    print("it's true")

# if + ifel and else
if 10 == 20: 
    print("10 is not same than 20")
elif 10 > 20 :
    print("20 is more less than 10")
else :
    print("all past affirmations were wrong") 

# short if + else in a one line 
print ('it  is true' ) if  800 > 1000 else print('it is false')


# use and and or 

if  2 > 1 and 5 > 4 :
    print("the both conditions are true")

if  4 > 2 and  len("hello") < len("bye"):
    print("if one condition is false")

if  10 > 50 or 80 < 40:
    print("if one condition is true, it'll show the message")

if 50 > 400 or 80 > 888 :
    print("if both condition are false, it will not show the message")




