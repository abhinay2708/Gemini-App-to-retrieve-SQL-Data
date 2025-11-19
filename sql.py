import sqlite3

#Connectt to SQlite
#Our database name: Naresh_it_student
connection=sqlite3.connect("employee.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

#create the table
#Our table name student
#Columns names are: name, course
table_info="""
Create table employee(employee_name varchar(30),
                    employee_role varchar(30),
                    employee_salary FLOAT);
"""
cursor.execute(table_info)

#Insert the records

cursor.execute('''Insert Into employee values('Abhinay','Data Science',750000)''')
cursor.execute('''Insert Into employee values('Abhinav','Data Science',90000)''')
cursor.execute('''Insert Into employee values('Ibtesham','Data Science',88000)''')
cursor.execute('''Insert Into employee values('Gourab','Data Engineer',50000)''')
cursor.execute('''Insert Into employee values('Pratikshya','Data Analyst',35000)''')
cursor.execute('''Insert Into employee values('Rajitha','Data Analyst',60000)''')

#Dispaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from employee''')
for row in data:
    print(row)

#Commit your changes int he databse
connection.commit()
connection.close()