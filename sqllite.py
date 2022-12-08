#creating database


import os
import sqlite3

db_filename= 'dipesh.db'
conn = sqlite3.connect(db_filename)

conn = sqlite3.connect('dipesh.db')
"""
conn.execute('drop table if exists staff')
print("Table staff Exists/Drop")


#creating Table
conn.execute('create table staff(ID int,Name text,Age int,Gender text)')
print("Table staff Created")

#insert Values
conn.execute('insert into staff(ID,Name,Age,Gender) values(0001,"Name 1",21,"M")')
conn.execute('insert into staff(ID,Name,Age,Gender) values(0002,"Name 2",28,"F")')
conn.execute('insert into staff(ID,Name,Age,Gender) values(0003,"Name 3",26,"M")')


conn.commit()
print("Rows are inserted in Table staff Created")

cursor = conn.cursor()

print("Displaying staff Created")
#cursor.execute('select * from staff')
#result = cursor.fetchall()
#result= cursor.fetchone()

result = conn.execute('select * from staff where gender =="M" ')
for rows in result:
    print(rows)

result = conn.execute('select Name,Age from staff')
for rows in result:
    print(rows)
"""
"""
conn.execute('drop table if exists student')
print("Table student Exists/Drop")

#creating Table
conn.execute('create table student(roll int, subject text, city text, phone int)')
print("Table student Created")

#insert values
conn.execute('insert into student( roll, subject, city,phone) values( 4564, "science", "ktm", 779463)')
conn.execute('insert into student( roll, subject, city,phone) values( 9932, "mgmt", "lalitpur", 888834)')
conn.execute('insert into student( roll, subject, city,phone) values( 7748, "law", "bhaktapur", 332555)')


conn.commit()
print("Rows are inserted in Table student Created")

cursor = conn.cursor()

print("Displaying student Created")
"""

"""
sql_update_query = "update student set city = 'kathmandu' where roll = 4564"

conn.execute(sql_update_query)

conn.commit()"""


result = conn.execute('select * from student')

for rows in result:
    print(rows)
