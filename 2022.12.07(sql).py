Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/sqllite.py

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/sqllite.py
Table staff Exists/Drop
Table staff Created

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/sqllite.py
Table staff Exists/Drop
Table staff Created
Rows are inserted in Table staff Created
Displaying staff Created
(1, 'Name 1', 21, 'M')
(2, 'Name 2', 28, 'F')
(3, 'Name 3', 26, 'M')

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/sqllite.py
Table staff Exists/Drop
Table staff Created
Rows are inserted in Table staff Created
Displaying staff Created
(1, 'Name 1', 21, 'M')
(3, 'Name 3', 26, 'M')

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/sqllite.py
(1, 'Name 1', 21, 'M')
(3, 'Name 3', 26, 'M')

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/sqllite.py
(1, 'Name 1', 21, 'M')
(3, 'Name 3', 26, 'M')
('Name 1', 21)
('Name 2', 28)
('Name 3', 26)

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/sqllite.py
(1, 'Name 1', 21, 'M')
(3, 'Name 3', 26, 'M')
('Name 1', 21)
('Name 2', 28)
('Name 3', 26)

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/sqllite.py
Table staff Exists/Drop
Table staff Created
Traceback (most recent call last):
  File "C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/sqllite.py", line 50, in <module>
    conn.execute('insert into staff(Student name, roll, subject, city,phone) values("ram", 4564, "science", "ktm", 779463)')
sqlite3.OperationalError: near "name": syntax error

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/sqllite.py
Table staff Exists/Drop
Table staff Created
Rows are inserted in Table staff Created
Displaying staff Created
Traceback (most recent call last):
  File "C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/sqllite.py", line 62, in <module>
    result = conn.execute('select * from staff where gender =="M" ')
sqlite3.OperationalError: no such column: gender

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/sqllite.py
Table staff Exists/Drop
Table staff Created
Rows are inserted in Table staff Created
Displaying staff Created
('ram', 4564, 'science', 'ktm', 779463)
('shyam', 9932, 'mgmt', 'lalitpur', 888834)
('hari', 7748, 'law', 'bhaktapur', 332555)

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/sqllite.py
Table staff Exists/Drop
Table staff Created
Traceback (most recent call last):
  File "C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/sqllite.py", line 50, in <module>
    conn.execute('insert into student( roll, subject, city,phone) values("ram", 4564, "science", "ktm", 779463)')
sqlite3.OperationalError: 5 values for 4 columns

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/sqllite.py
Table staff Exists/Drop
Traceback (most recent call last):
  File "C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/sqllite.py", line 46, in <module>
    conn.execute('create table student(roll int, subject text, city text, phone int)')
sqlite3.OperationalError: table student already exists

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/sqllite.py
Table student Exists/Drop
Table student Created
Traceback (most recent call last):
  File "C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/sqllite.py", line 50, in <module>
    conn.execute('insert into student( roll, subject, city,phone) values("ram", 4564, "science", "ktm", 779463)')
sqlite3.OperationalError: 5 values for 4 columns

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/sqllite.py
Table student Exists/Drop
Table student Created
Rows are inserted in Table student Created
Displaying student Created
(4564, 'science', 'ktm', 779463)
(9932, 'mgmt', 'lalitpur', 888834)
(7748, 'law', 'bhaktapur', 332555)

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/sqllite.py
Table student Exists/Drop
Table student Created
Rows are inserted in Table student Created
Displaying student Created
(4564, 'science', 'ktm', 779463)
(9932, 'mgmt', 'lalitpur', 888834)
(7748, 'law', 'bhaktapur', 332555)

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/sqllite.py
(4564, 'science', 'ktm', 779463)
(9932, 'mgmt', 'lalitpur', 888834)
(7748, 'law', 'bhaktapur', 332555)

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/sqllite.py
(4564, 'science', 'ktm', 779463)
(9932, 'mgmt', 'lalitpur', 888834)
(7748, 'law', 'bhaktapur', 332555)

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/sqllite.py
(4564, 'science', 'ktm', 779463)
(9932, 'mgmt', 'lalitpur', 888834)
(7748, 'law', 'bhaktapur', 332555)

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/sqllite.py
(4564, 'science', 'ktm', 779463)
(9932, 'mgmt', 'lalitpur', 888834)
(7748, 'law', 'bhaktapur', 332555)
>>> 
= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/sqllite.py
(4564, 'science', 'ktm', 779463)
(9932, 'mgmt', 'lalitpur', 888834)
(7748, 'law', 'bhaktapur', 332555)
>>> 
= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/sqllite.py
(4564, 'science', 'ktm', 779463)
(9932, 'mgmt', 'lalitpur', 888834)
(7748, 'law', 'bhaktapur', 332555)
>>> 
= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/sqllite.py
(4564, 'science', 'kathmandu', 779463)
(9932, 'mgmt', 'lalitpur', 888834)
(7748, 'law', 'bhaktapur', 332555)
>>> 
= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/sqllite.py
(4564, 'science', 'kathmandu', 779463)
(9932, 'mgmt', 'lalitpur', 888834)
(7748, 'law', 'bhaktapur', 332555)
>>> 
= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/sql(a).py
Table student Exists/Drop
Table student Created
Rows are inserted in Table student Created
Displaying student Created
(4564, 'science', 'ktm', 779463)
(9932, 'mgmt', 'lalitpur', 888834)
(7748, 'law', 'bhaktapur', 332555)
>>> 
= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/sql(a).py
(9932, 'mgmt', 'lalitpur', 888834)
(7748, 'law', 'bhaktapur', 332555)
>>> 
= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/sql(a).py
(9932, 'mgmt', 'lalitpur', 888834)
(7748, 'law', 'bhaktapur', 332555)
