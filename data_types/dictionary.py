#define a dictionary

new_dictionary = {
    "name":"Isaac",
    5:"dog",
    "names":[
        "Isaac",
        "Alex",
        "Nadia"
    ]
}

print(new_dictionary);

new_dictionary2 = dict(name="PEDRO", table ={ "width":50, "height":20})
print(new_dictionary2)

#access to a specific element
name = new_dictionary['name']
names = new_dictionary.get('names')
print(name)
print(names)

#added new element 
new_dictionary['last_names'] = [
    "Perez",
    "Gomez"
]
print(new_dictionary)

# know the dictionary's length
print(len(new_dictionary))

# ways to delete a from the array
#new_dictionary.pop('last_name');
# new_dictionary.popitem() delete the last element from array
del new_dictionary['last_names']
print(new_dictionary)

# copy the dictionary
new_dictionary.popitem()
backup_dictionary =  new_dictionary.copy()
backup_dictionary = dict(new_dictionary) # other way to copy a dictionary
print(backup_dictionary)

#delete the dictionary 
new_dictionary.clear()
