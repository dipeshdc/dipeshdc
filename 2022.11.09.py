Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/2022.12.09(gen).py
MainList:  [12, 34, 67, 89, 0, 1, 2, 3, 4]
Normal Function TEST
<class 'list'>
[12, 34, 67, 89, 0, 1, 2, 3, 4]


Yield Generator Test
<class 'generator'>
[14, 36, 69, 91, 2, 3, 4, 5, 6]

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/2022.12.09(gen).py
MainList:  [12, 34, 67, 89, 0, 1, 2, 3, 4]
Normal Function TEST
<class 'list'>
[12, 34, 67, 89, 0, 1, 2, 3, 4]


Yield Generator Test
<class 'generator'>
[12, 34, 67, 89, 0, 1, 2, 3, 4]
>>> 
= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/2022.12.09(gen).py
MainList:  [12, 34, 67, 89, 0, 1, 2, 3, 4]
Normal Function TEST
<class 'list'>
[12, 34, 67, 89, 0, 1, 2, 3, 4]


Yield Generator Test
<class 'generator'>
[10, 32, 65, 87, -2, -1, 0, 1, 2]
>>> 
>>> def check():
...     yield 10
...     yield 20
...     yield "python"
... 
...     
>>> print(list(check)())
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(list(check)())
TypeError: 'function' object is not iterable
>>> print(list(check()))
[10, 20, 'python']
>>> 
>>> 
>>> import numpy
>>> dir(numpy)

