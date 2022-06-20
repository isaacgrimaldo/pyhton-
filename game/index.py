new_data = input('set new value: ')

data_base = ['bye', 'hello', 'new message',  'programming']

if data_base.count(new_data) > 0 :
    print('this info already exist in the data base')
    print(data_base)
else :
    data_base.append(new_data)
    print(data_base) 