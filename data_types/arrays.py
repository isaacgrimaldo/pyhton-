# define a new list 
list = [1,2,3,4,5,67,89]
print(list)

#add new element 
list.append(50)

# clear list
# list.clear()

#  array's length
lenght = len(list)
print(lenght)

# know how many time, number is repite in the list
count =  list.count(4)
print(count)

# access at specific element in the array
first_element = list[0]
print(first_element)

# delete the laster element in the list
list.pop()
print(list)

# delete a element with specific value 
list.remove(4)
print(list)

# order the element in the list, min to max
list.sort()
print(list)

#inverted the array
list.reverse()
print(list)

# copy the dictionary
copy = list.copy();
print(copy)