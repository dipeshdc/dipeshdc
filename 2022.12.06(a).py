Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

== RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/reeg.py =
Match 1 was found at 4-7: cat
Match 2 was found at 8-11: sat
Match 3 was found at 19-22: mat

== RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/reeg.py =
Match 1 was found at 4-7: cat
Match 2 was found at 8-11: sat
Match 3 was found at 19-22: mat
Match 1 was found at 11-15:  on 
Group 1 found at 12-14: on

= RESTART: C:/Users/HP/AppData/Local/Programs/Python/Python310/CO2022/reeg11.py
Match 1 was found at 247-258: validation.
Group 1 found at 247-257: validation


squares = []
main = []
for num in range(20):
    main.append(num**2)
print("main:", main)
SyntaxError: invalid syntax
for num in range(20):
    main.append(num**2)
    print("main:", main)

    
main: [0]
main: [0, 1]
main: [0, 1, 4]
main: [0, 1, 4, 9]
main: [0, 1, 4, 9, 16]
main: [0, 1, 4, 9, 16, 25]
main: [0, 1, 4, 9, 16, 25, 36]
main: [0, 1, 4, 9, 16, 25, 36, 49]
main: [0, 1, 4, 9, 16, 25, 36, 49, 64]
main: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
main: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
main: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
main: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]
main: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169]
main: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
main: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]
main: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256]
main: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289]
main: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324]
main: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
[x**2 for  x in range(20)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
for num in range(20):
    main.append(num**2)

    
print("main:", main)
main: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
[x**2 for  x in range(20)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
for num in range(10):
    main.append(num**2)

    
print("main:", main)
main: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
even_comp = [x for x in range(30) if x % 3 == 0]
print("[x for x in range(30) if x % 3 == 0]>>", even_comp)
[x for x in range(30) if x % 3 == 0]>> [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
cube_squares = [x**2 if x % 2 == 0 else x**3 for x in range(20)]
print("[x**2 if x % 2 == 0 else x**3 for x in range(20)] >> ",cube_squares)
[x**2 if x % 2 == 0 else x**3 for x in range(20)] >>  [0, 1, 4, 27, 16, 125, 36, 343, 64, 729, 100, 1331, 144, 2197, 196, 3375, 256, 4913, 324, 6859]



l = list(range(1,100,5))
for x,y in enumerate(l):
    prit(x, "::", y)

    
Traceback (most recent call last):
  File "<pyshell#31>", line 2, in <module>
    prit(x, "::", y)
NameError: name 'prit' is not defined. Did you mean: 'print'?
l = list(range(1,100,5))
for x,y in enumerate(l):
    print(x, "::", y)
    
SyntaxError: multiple statements found while compiling a single statement

for x,y in enumerate(l):
    print(x, "::", y)

    
0 :: 1
1 :: 6
2 :: 11
3 :: 16
4 :: 21
5 :: 26
6 :: 31
7 :: 36
8 :: 41
9 :: 46
10 :: 51
11 :: 56
12 :: 61
13 :: 66
14 :: 71
15 :: 76
16 :: 81
17 :: 86
18 :: 91
19 :: 96
>>> print("\nDict CUBES : ",{x: x**3 for x in range(20)})

Dict CUBES :  {0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000, 11: 1331, 12: 1728, 13: 2197, 14: 2744, 15: 3375, 16: 4096, 17: 4913, 18: 5832, 19: 6859}
>>> print("Dict CUBES EVEN: ",{x: x**3 for x in range(10) if x**3 % 2 == 0})
Dict CUBES EVEN:  {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}
>>> print("Dict CUBES EVEN: ",[x: x**3 for x in range(10) if x**3 % 2 == 0])
SyntaxError: invalid syntax
>>> print("Dict CUBES EVEN: ",{x: x**3 for x in range(10) if x**3 % 2 == 0})
Dict CUBES EVEN:  {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}
>>> 
>>> 
>>> i = (str(i) for i in range(10))
>>> print(list(i))
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> 
>>> print([for i in range(10)])
SyntaxError: invalid syntax
>>> print([i for i in range(10)])
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> print([str(i) for i in range(10)])
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
