import os
import sqlite3

db_filename= 'dipesh.db'
conn = sqlite3.connect(db_filename)

conn = sqlite3.connect('dipesh.db')
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


conn.execute("DELETE from student where roll = 4564")
conn.commit()
"""
result = conn.execute('select * from student')

for rows in result:
    print(rows)
