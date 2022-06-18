# define a tupla

tupla = ("hello", "bye", "good night", "good afternoon")
print(tupla)

#access to specific value with a index 
element_2 = tupla[1]
print(element_2)

#know how many times a number is repite into the array
hello_nums = tupla.count('hello')
print(hello_nums)

#know the array's length 
length = len(tupla)
print(length)

#when you are working  with tuplas  the method append no exist in them
# tupla.append(value) => error

# the only way to added a new element it's  become the tupla to an array  
new_list = list(tupla)
new_list.append("good evening")
print(new_list)