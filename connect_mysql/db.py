import mysql.connector

mysqlDB = mysql.connector.connect(
    host='localhost',
    user='root',
    password='my-secret-pw',
    database='test',
    port=8000
)

# see the table structure
see_table_structure = 'show create table Users'

# create a query to automatize the create new user process
set_new_user = 'insert into Users (name, email, age) values (%s, %s, %s)'
values = ('Test','test@test', 20)

#upgrade registers
upgrade_registers = 'update Users set email = %s where name = %s'
upgrade_values = ('pedroTest@test.com', 'pedro') 

#delete registers
delete_register = 'delete from Users where name = %s'
delete_values = ('Test',)

slq = mysqlDB.cursor()

# see the response of the query
slq.execute(see_table_structure)
result = slq.fetchall()

## the response to create new user
slq.execute(set_new_user , values)
mysqlDB.commit() # save the values sent them , always that you send information to the data base, you have execute commit() 
print(slq.rowcount) # return the new row number saved in the data base

# upgrade a column email
slq.execute(upgrade_registers, upgrade_values)
mysqlDB.commit() 

#delete a register
slq.execute(delete_register,  delete_values)
mysqlDB.commit()

# first test
# slq.execute('select * from Users')
# result = slq.fetchone()