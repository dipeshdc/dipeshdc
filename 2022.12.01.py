Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
y = "antartica"
print(y)
antartica
dir(y)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
help(y.strip)
Help on built-in function strip:

strip(chars=None, /) method of builtins.str instance
    Return a copy of the string with leading and trailing whitespace removed.
    
    If chars is given and not None, remove characters in chars instead.

help(y.split)
Help on built-in function split:

split(sep=None, maxsplit=-1) method of builtins.str instance
    Return a list of the substrings in the string, using sep as the separator string.
    
      sep
        The separator used to split the string.
    
        When set to None (the default value), will split on any whitespace
        character (including \\n \\r \\t \\f and spaces) and will discard
        empty strings from the result.
      maxsplit
        Maximum number of splits (starting from the left).
        -1 (the default value) means no limit.
    
    Note, str.split() is mainly useful for data that has been intentionally
    delimited.  With natural text that includes punctuation, consider using
    the regular expression module.

y.split()
['antartica']
y.split(4)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    y.split(4)
TypeError: must be str or None, not int
y = "antartica is very cold."
y.split()
['antartica', 'is', 'very', 'cold.']
y.split( )
['antartica', 'is', 'very', 'cold.']
y.split(a)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    y.split(a)
NameError: name 'a' is not defined
y.split(/)
SyntaxError: invalid syntax
y.split(\)
    
SyntaxError: unexpected character after line continuation character
y.split()
['antartica', 'is', 'very', 'cold.']
# IT HAS A OPTION FOR COMMENT IN PYTHON.
y.split('c')
['antarti', 'a is very ', 'old.']
y.split()
['antartica', 'is', 'very', 'cold.']
y.split()
['antartica', 'is', 'very', 'cold.']
#
y.split()   # chopping
['antartica', 'is', 'very', 'cold.']
z= "i am very graceful./n and i am now in a lab.
SyntaxError: incomplete input
z= "i am very graceful./n and i am now in a lab."
print(z)
i am very graceful./n and i am now in a lab.
z= "i am very graceful.\n and i am now in a lab."
print(z)
i am very graceful.
 and i am now in a lab.
i am very graceful./n and i am now in a lab.
SyntaxError: invalid syntax
z= "i am very graceful./nand i am now in a lab."
print(z)
i am very graceful./nand i am now in a lab.
z= "i am very graceful./n and i am now in a lab."
print(z)
i am very graceful./n and i am now in a lab.
z= "i am very graceful.\n and i am now in a lab."
print(z)
i am very graceful.
 and i am now in a lab.
z= "i am very graceful.\nand i am now in a lab."
print(z)
i am very graceful.
and i am now in a lab.
z= "i am very graceful.\n and i am now in a lab."
print(z)
i am very graceful.
 and i am now in a lab.
z
'i am very graceful.\n and i am now in a lab.'
print(z)
i am very graceful.
 and i am now in a lab.
z= "i am very graceful.\t and i am now in a lab."
print(z)
i am very graceful.	 and i am now in a lab.
z= "i am very graceful.\tand i am now in a lab."
print(z)
i am very graceful.	and i am now in a lab.

z= "i am very graceful. \t and i am now in a lab."
print(z)
i am very graceful. 	 and i am now in a lab.
z.count()
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    z.count()
TypeError: count() takes at least 1 argument (0 given)
z.count( )
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    z.count( )
TypeError: count() takes at least 1 argument (0 given)
z.count(" ")
11
z.count("\t")
1
u = "aana\salld"
print(u)
aana\salld
u = "aana\Salld"
print(u)
aana\Salld
u = "aana\salld"
u = "aana/salld"
print(u)
aana/salld
u = "aana\salld"
print(u)
aana\salld
letters = "jfs  jfj jls mea  ajaa aanjah auul  faflacj flsi siaoiufa a fnf fjfjsuc uva fua f ajafjflfjfn  ulf au jljfon juofuf jk r fsaiuff fjfjof fjfsufoiuf fsfoifj fj   jjfjljlfufojflk w"
print(letters)
jfs  jfj jls mea  ajaa aanjah auul  faflacj flsi siaoiufa a fnf fjfjsuc uva fua f ajafjflfjfn  ulf au jljfon juofuf jk r fsaiuff fjfjof fjfsufoiuf fsfoifj fj   jjfjljlfufojflk w
letters=""" jfs jfskf f j f jjljfuoifj ou uoujljljf njhu089wuojrlw u974 ioncyvvy97 9oijjsu798r 98ns by9yhfkjhff jfs  jfj jls mea  ajaa aanjah auul  faflacj flsi siaoiufa a fnf fjfjsuc uva fua f ajafjflfjfn  ulf au jljfon juofuf jk r fsaiuff fjfjof fjfsufoiuf fsfoifj fj   jjfjljlfufojflk w f osnyffh"""
print(letters)
 jfs jfskf f j f jjljfuoifj ou uoujljljf njhu089wuojrlw u974 ioncyvvy97 9oijjsu798r 98ns by9yhfkjhff jfs  jfj jls mea  ajaa aanjah auul  faflacj flsi siaoiufa a fnf fjfjsuc uva fua f ajafjflfjfn  ulf au jljfon juofuf jk r fsaiuff fjfjof fjfsufoiuf fsfoifj fj   jjfjljlfufojflk w f osnyffh
letters=""" jfs jfskf f j f jjljfuoifj ou uoujljljf njhu089wuojrlw u974 ioncyvvy97 9oijjsu798r 98ns by9yhfkjhff jfs  jfj jls mea  ajaa aanjah auul  faflacj flsi siaoiufa a fnf fjfjsuc uva fua f ajafjflfjfn  ulf au jljfon juofuf jk r fsaiuff fjfjof fjfsufoiuf fsfoifj fj   jjfjljlfufojflk w f osnyffh"""
letters=""" jfs jfskf f j f jjljfuoifj ou uoujljljf njhu089wuojrlw u974 ioncyvvy97 9oijjsu798r 98ns by9yhfkjhff jfs  jfj jls mea  ajaa aanjah auul  faflacj flsi siaoiufa a fnf fjfjsuc uva fua f ajafjflfjfn  ulf au jljfon juofuf jk r fsaiuff fjfjof fjfsufoiuf fsfoifj fj   jjfjljlfufojflk w f osnyffh
andf al
ajksjs\
 jlkljlojljf fjf sfl fs
   f ljlj jlja;lj
    jlf j
    jljll
    js
    a

    aj"""
print(letters)
 jfs jfskf f j f jjljfuoifj ou uoujljljf njhu089wuojrlw u974 ioncyvvy97 9oijjsu798r 98ns by9yhfkjhff jfs  jfj jls mea  ajaa aanjah auul  faflacj flsi siaoiufa a fnf fjfjsuc uva fua f ajafjflfjfn  ulf au jljfon juofuf jk r fsaiuff fjfjof fjfsufoiuf fsfoifj fj   jjfjljlfufojflk w f osnyffh
andf al
ajksjs jlkljlojljf fjf sfl fs
   f ljlj jlja;lj
    jlf j
    jljll
    js
    a

    aj

""" jfs jfskf f j f jjljfuoifj ou uoujljljf njhu089wuojrlw u974 ioncyvvy97 9oijjsu798r 98ns by9yhfkjhff jfs  jfj jls mea  ajaa aanjah auul  faflacj flsi siaoiufa a fnf fjfjsuc uva fua f ajafjflfjfn  ulf au jljfon juofuf jk r fsaiuff fjfjof fjfsufoiuf fsfoifj fj   jjfjljlfufojflk w f osnyffh
andf al
ajksjs\
 jlkljlojljf fjf sfl fs
   f ljlj jlja;lj
    jlf j
    jljll
    js
    a

    aj"""
' jfs jfskf f j f jjljfuoifj ou uoujljljf njhu089wuojrlw u974 ioncyvvy97 9oijjsu798r 98ns by9yhfkjhff jfs  jfj jls mea  ajaa aanjah auul  faflacj flsi siaoiufa a fnf fjfjsuc uva fua f ajafjflfjfn  ulf au jljfon juofuf jk r fsaiuff fjfjof fjfsufoiuf fsfoifj fj   jjfjljlfufojflk w f osnyffh\nandf al\najksjs jlkljlojljf fjf sfl fs\n   f ljlj jlja;lj\n    jlf j\n    jljll\n    js\n    a\n\n    aj'
letters.count(" ")
83
letters.count("a")
25
letters.count("l")
28
age =20
if age>30:
age=20
SyntaxError: expected an indented block after 'if' statement on line 1
age =20
age=20
b=33
if b>20:
print(true)
SyntaxError: expected an indented block after 'if' statement on line 1
if b>20 :
    print("ok")

ok

b=23
print(b=23)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    print(b=23)
TypeError: 'b' is an invalid keyword argument for print()
print("b=23")
b=23
b=33
if b>20:
    print("It is ok")

It is ok
if b<20:
    print("It is ok")
else:
    print("it is not ok")

    
it is not ok
if b<44:
    print("It is ok")
else:
    print("it is not ok")

    
It is ok
a=5
if a==10:
    print("yes")
else:
    print("no")

    
no
a==10
False
a==10|| a<=4
SyntaxError: invalid syntax
a==10|| a<=4
SyntaxError: invalid syntax
a==10| a<=4
False
a==10 or a<=4
False
a==10 and/or a<=4
SyntaxError: invalid syntax
a==10 and a<=4
False
a==10 & a<=4
False
a==10 and a<=4
False
a==10 or a<=4
False
a==10 or a<=8
True
if a==10 & a<=8
    print("yeah, you are ok with that")
else:
    print("no, you can't be ok with this")
    
SyntaxError: expected ':'

if a==10 & a<=8:
    print("yeah, you are ok with that")
else:
    print("no, you can't be ok with this")

    
no, you can't be ok with this
if a==10 | a<=8:
    print("yeah, you are ok with that")
else:
    print("no, you can't be ok with this")

    
no, you can't be ok with this
if a==10 & a<=8 & a >4:
    print("yeah, you are ok with that")
else:
    print("no, you can't be ok with this")

    
no, you can't be ok with this
if a==10 | a<=8 | a >4:
    print("yeah, you are ok with that")
else:
    print("no, you can't be ok with this")

    
no, you can't be ok with this
if a==10 | a<=8 | a >4:
    print("yeah, you are ok with that")
else:
    print("no, you can't be ok with this")

    
no, you can't be ok with this
if a==10 & a<=8 & a >4:
    print("yeah, you are ok with that")
elif(a>10 and a>7)
    print("yeah, you are ok with that")
elif(a<=10 and a>=12)
    print("yeah, you are ok with that")
else:
    print("no, you can't be ok with this")
    
SyntaxError: expected ':'

if a==10 & a<=8 & a >4:
    print("yeah, you are ok with that")
elif(a>10 and a>7):
    print("yeah, you are ok with that")
elif(a<=10 and a>=12):
    print("yeah, you are ok with that")
else:
    print("no, you can't be ok with this")

    
no, you can't be ok with this
if a==10 or a<=8 or a >4:
    print("yeah, you are ok with that")
elif(a>10 or a>7):
    print("yeah, you are ok with that")
elif(a<=10 or a>=12):
    print("yeah, you are ok with that")
else:
    print("no, you can't be ok with this")

    
yeah, you are ok with that

name = "python"
't' in name
True
for 'o' in name:
    
SyntaxError: cannot assign to literal
for t in name:
    print(true)

    
Traceback (most recent call last):
  File "<pyshell#158>", line 2, in <module>
    print(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
for t in name:
    print("you are 100% right")

    
you are 100% right
you are 100% right
you are 100% right
you are 100% right
you are 100% right
you are 100% right
for t in name:
    print("you are 100% right")

    
you are 100% right
you are 100% right
you are 100% right
you are 100% right
you are 100% right
you are 100% right
for char in name:
    print("t")

    
t
t
t
t
t
t
for t in name:
    print("you are 100% right")

    
you are 100% right
you are 100% right
you are 100% right
you are 100% right
you are 100% right
you are 100% right
for char in name:
    print("t")

    
t
t
t
t
t
t
for char in name:
    print(t)

    
n
n
n
n
n
n
for char in name:
    print(char)

    
p
y
t
h
o
n
for i in range(190):
    print(i)

    
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
for i in range(10,100):
    if i>25:
    print(i+25)
    
SyntaxError: expected an indented block after 'if' statement on line 2
for i in range(10,100):
    if i>25:
        print(i+25)
    if (i=50):
        
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
for i in range(10,100):
    if i>25:
        print(i+25)
    if (i=50):
        
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
for i in range(10,100):
    if i>25:
        print(i+25)
    if (i==50):
        print("fifty")
    if (i>=80):
        print("eightees ")

        
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
fifty
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
eightees 
106
eightees 
107
eightees 
108
eightees 
109
eightees 
110
eightees 
111
eightees 
112
eightees 
113
eightees 
114
eightees 
115
eightees 
116
eightees 
117
eightees 
118
eightees 
119
eightees 
120
eightees 
121
eightees 
122
eightees 
123
eightees 
124
eightees 
for i in range(10,100):
    if i>25:
        print(i+"25")
    if (i==50):
        print("fifty")
    if (i>=80):
        print("eightees ")

        
Traceback (most recent call last):
  File "<pyshell#187>", line 3, in <module>
    print(i+"25")
TypeError: unsupported operand type(s) for +: 'int' and 'str'
for i in range(10,100):
    if i>25:
        print(i+"str(25)")
    if (i==50):
        print("fifty")
    if (i>=80):
        print("eightees ")

        
Traceback (most recent call last):
  File "<pyshell#189>", line 3, in <module>
    print(i+"str(25)")
TypeError: unsupported operand type(s) for +: 'int' and 'str'
for i in range(10,100):
    if i>25:
        print(i+"int(25)")
    if (i==50):
        print("fifty")
    if (i>=80):
        print("eightees ")

        
Traceback (most recent call last):
  File "<pyshell#191>", line 3, in <module>
    print(i+"int(25)")
TypeError: unsupported operand type(s) for +: 'int' and 'str'
for i in range(10,100):
    if i>25:
        print(i+"25")
    if (i==50):
        print("fifty")
    if (i>=80):
        print("eightees ")

        
Traceback (most recent call last):
  File "<pyshell#193>", line 3, in <module>
    print(i+"25")
TypeError: unsupported operand type(s) for +: 'int' and 'str'
for i in range(10,100):
    if i>25:
        print(str(i)+"25")
    if (i==50):
        print("fifty")
    if (i>=80):
        print("eightees ")

        
2625
2725
2825
2925
3025
3125
3225
3325
3425
3525
3625
3725
3825
3925
4025
4125
4225
4325
4425
4525
4625
4725
4825
4925
5025
fifty
5125
5225
5325
5425
5525
5625
5725
5825
5925
6025
6125
6225
6325
6425
6525
6625
6725
6825
6925
7025
7125
7225
7325
7425
7525
7625
7725
7825
7925
8025
eightees 
8125
eightees 
8225
eightees 
8325
eightees 
8425
eightees 
8525
eightees 
8625
eightees 
8725
eightees 
8825
eightees 
8925
eightees 
9025
eightees 
9125
eightees 
9225
eightees 
9325
eightees 
9425
eightees 
9525
eightees 
9625
eightees 
9725
eightees 
9825
eightees 
9925
eightees 
for i in range(10,100):
    if i>25:
        print(str(i)+" -- 25")
    if (i==50):
        print("fifty")
    if (i>=80):
        print("eightees ")

        
26 -- 25
27 -- 25
28 -- 25
29 -- 25
30 -- 25
31 -- 25
32 -- 25
33 -- 25
34 -- 25
35 -- 25
36 -- 25
37 -- 25
38 -- 25
39 -- 25
40 -- 25
41 -- 25
42 -- 25
43 -- 25
44 -- 25
45 -- 25
46 -- 25
47 -- 25
48 -- 25
49 -- 25
50 -- 25
fifty
51 -- 25
52 -- 25
53 -- 25
54 -- 25
55 -- 25
56 -- 25
57 -- 25
58 -- 25
59 -- 25
60 -- 25
61 -- 25
62 -- 25
63 -- 25
64 -- 25
65 -- 25
66 -- 25
67 -- 25
68 -- 25
69 -- 25
70 -- 25
71 -- 25
72 -- 25
73 -- 25
74 -- 25
75 -- 25
76 -- 25
77 -- 25
78 -- 25
79 -- 25
80 -- 25
eightees 
81 -- 25
eightees 
82 -- 25
eightees 
83 -- 25
eightees 
84 -- 25
eightees 
85 -- 25
eightees 
86 -- 25
eightees 
87 -- 25
eightees 
88 -- 25
eightees 
89 -- 25
eightees 
90 -- 25
eightees 
91 -- 25
eightees 
92 -- 25
eightees 
93 -- 25
eightees 
94 -- 25
eightees 
95 -- 25
eightees 
96 -- 25
eightees 
97 -- 25
eightees 
98 -- 25
eightees 
99 -- 25
eightees 
for i in range(10,100):
    if i>25:
        print(str(i)+" -- 25")
    if (i==50):
        print("fifty")
    if (i>=80):
        print("eightees ")
    if (i>=80):
        if (i<=90):
            print(i)

            
26 -- 25
27 -- 25
28 -- 25
29 -- 25
30 -- 25
31 -- 25
32 -- 25
33 -- 25
34 -- 25
35 -- 25
36 -- 25
37 -- 25
38 -- 25
39 -- 25
40 -- 25
41 -- 25
42 -- 25
43 -- 25
44 -- 25
45 -- 25
46 -- 25
47 -- 25
48 -- 25
49 -- 25
50 -- 25
fifty
51 -- 25
52 -- 25
53 -- 25
54 -- 25
55 -- 25
56 -- 25
57 -- 25
58 -- 25
59 -- 25
60 -- 25
61 -- 25
62 -- 25
63 -- 25
64 -- 25
65 -- 25
66 -- 25
67 -- 25
68 -- 25
69 -- 25
70 -- 25
71 -- 25
72 -- 25
73 -- 25
74 -- 25
75 -- 25
76 -- 25
77 -- 25
78 -- 25
79 -- 25
80 -- 25
eightees 
80
81 -- 25
eightees 
81
82 -- 25
eightees 
82
83 -- 25
eightees 
83
84 -- 25
eightees 
84
85 -- 25
eightees 
85
86 -- 25
eightees 
86
87 -- 25
eightees 
87
88 -- 25
eightees 
88
89 -- 25
eightees 
89
90 -- 25
eightees 
90
91 -- 25
eightees 
92 -- 25
eightees 
93 -- 25
eightees 
94 -- 25
eightees 
95 -- 25
eightees 
96 -- 25
eightees 
97 -- 25
eightees 
98 -- 25
eightees 
99 -- 25
eightees 
for i in range(10,100):
    if i>25:
        print(str(i)+" -- 25")
    if (i==50):
        print("fifty")
    if (i>=80):
        if (i<=90):
            print(i)

            
26 -- 25
27 -- 25
28 -- 25
29 -- 25
30 -- 25
31 -- 25
32 -- 25
33 -- 25
34 -- 25
35 -- 25
36 -- 25
37 -- 25
38 -- 25
39 -- 25
40 -- 25
41 -- 25
42 -- 25
43 -- 25
44 -- 25
45 -- 25
46 -- 25
47 -- 25
48 -- 25
49 -- 25
50 -- 25
fifty
51 -- 25
52 -- 25
53 -- 25
54 -- 25
55 -- 25
56 -- 25
57 -- 25
58 -- 25
59 -- 25
60 -- 25
61 -- 25
62 -- 25
63 -- 25
64 -- 25
65 -- 25
66 -- 25
67 -- 25
68 -- 25
69 -- 25
70 -- 25
71 -- 25
72 -- 25
73 -- 25
74 -- 25
75 -- 25
76 -- 25
77 -- 25
78 -- 25
79 -- 25
80 -- 25
80
81 -- 25
81
82 -- 25
82
83 -- 25
83
84 -- 25
84
85 -- 25
85
86 -- 25
86
87 -- 25
87
88 -- 25
88
89 -- 25
89
90 -- 25
90
91 -- 25
92 -- 25
93 -- 25
94 -- 25
95 -- 25
96 -- 25
97 -- 25
98 -- 25
99 -- 25
for i in range(10,100):
    if (i%2==0)
    
SyntaxError: incomplete input
for i in range(10,100):
    if (i%2==0):
        print("**")
        print(i)
        for x in range(i):
            print("++")
            print(x)

            
**
10
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
**
12
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
**
14
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
**
16
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
**
18
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
**
20
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
**
22
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
**
24
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
**
26
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
**
28
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
**
30
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
**
32
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
**
34
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
**
36
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
**
38
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
++
36
++
37
**
40
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
++
36
++
37
++
38
++
39
**
42
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
++
36
++
37
++
38
++
39
++
40
++
41
**
44
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
++
36
++
37
++
38
++
39
++
40
++
41
++
42
++
43
**
46
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
++
36
++
37
++
38
++
39
++
40
++
41
++
42
++
43
++
44
++
45
**
48
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
++
36
++
37
++
38
++
39
++
40
++
41
++
42
++
43
++
44
++
45
++
46
++
47
**
50
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
++
36
++
37
++
38
++
39
++
40
++
41
++
42
++
43
++
44
++
45
++
46
++
47
++
48
++
49
**
52
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
++
36
++
37
++
38
++
39
++
40
++
41
++
42
++
43
++
44
++
45
++
46
++
47
++
48
++
49
++
50
++
51
**
54
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
++
36
++
37
++
38
++
39
++
40
++
41
++
42
++
43
++
44
++
45
++
46
++
47
++
48
++
49
++
50
++
51
++
52
++
53
**
56
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
++
36
++
37
++
38
++
39
++
40
++
41
++
42
++
43
++
44
++
45
++
46
++
47
++
48
++
49
++
50
++
51
++
52
++
53
++
54
++
55
**
58
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
++
36
++
37
++
38
++
39
++
40
++
41
++
42
++
43
++
44
++
45
++
46
++
47
++
48
++
49
++
50
++
51
++
52
++
53
++
54
++
55
++
56
++
57
**
60
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
++
36
++
37
++
38
++
39
++
40
++
41
++
42
++
43
++
44
++
45
++
46
++
47
++
48
++
49
++
50
++
51
++
52
++
53
++
54
++
55
++
56
++
57
++
58
++
59
**
62
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
++
36
++
37
++
38
++
39
++
40
++
41
++
42
++
43
++
44
++
45
++
46
++
47
++
48
++
49
++
50
++
51
++
52
++
53
++
54
++
55
++
56
++
57
++
58
++
59
++
60
++
61
**
64
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
++
36
++
37
++
38
++
39
++
40
++
41
++
42
++
43
++
44
++
45
++
46
++
47
++
48
++
49
++
50
++
51
++
52
++
53
++
54
++
55
++
56
++
57
++
58
++
59
++
60
++
61
++
62
++
63
**
66
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
++
36
++
37
++
38
++
39
++
40
++
41
++
42
++
43
++
44
++
45
++
46
++
47
++
48
++
49
++
50
++
51
++
52
++
53
++
54
++
55
++
56
++
57
++
58
++
59
++
60
++
61
++
62
++
63
++
64
++
65
**
68
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
++
36
++
37
++
38
++
39
++
40
++
41
++
42
++
43
++
44
++
45
++
46
++
47
++
48
++
49
++
50
++
51
++
52
++
53
++
54
++
55
++
56
++
57
++
58
++
59
++
60
++
61
++
62
++
63
++
64
++
65
++
66
++
67
**
70
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
++
36
++
37
++
38
++
39
++
40
++
41
++
42
++
43
++
44
++
45
++
46
++
47
++
48
++
49
++
50
++
51
++
52
++
53
++
54
++
55
++
56
++
57
++
58
++
59
++
60
++
61
++
62
++
63
++
64
++
65
++
66
++
67
++
68
++
69
**
72
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
++
36
++
37
++
38
++
39
++
40
++
41
++
42
++
43
++
44
++
45
++
46
++
47
++
48
++
49
++
50
++
51
++
52
++
53
++
54
++
55
++
56
++
57
++
58
++
59
++
60
++
61
++
62
++
63
++
64
++
65
++
66
++
67
++
68
++
69
++
70
++
71
**
74
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
++
36
++
37
++
38
++
39
++
40
++
41
++
42
++
43
++
44
++
45
++
46
++
47
++
48
++
49
++
50
++
51
++
52
++
53
++
54
++
55
++
56
++
57
++
58
++
59
++
60
++
61
++
62
++
63
++
64
++
65
++
66
++
67
++
68
++
69
++
70
++
71
++
72
++
73
**
76
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
++
36
++
37
++
38
++
39
++
40
++
41
++
42
++
43
++
44
++
45
++
46
++
47
++
48
++
49
++
50
++
51
++
52
++
53
++
54
++
55
++
56
++
57
++
58
++
59
++
60
++
61
++
62
++
63
++
64
++
65
++
66
++
67
++
68
++
69
++
70
++
71
++
72
++
73
++
74
++
75
**
78
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
++
36
++
37
++
38
++
39
++
40
++
41
++
42
++
43
++
44
++
45
++
46
++
47
++
48
++
49
++
50
++
51
++
52
++
53
++
54
++
55
++
56
++
57
++
58
++
59
++
60
++
61
++
62
++
63
++
64
++
65
++
66
++
67
++
68
++
69
++
70
++
71
++
72
++
73
++
74
++
75
++
76
++
77
**
80
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
++
36
++
37
++
38
++
39
++
40
++
41
++
42
++
43
++
44
++
45
++
46
++
47
++
48
++
49
++
50
++
51
++
52
++
53
++
54
++
55
++
56
++
57
++
58
++
59
++
60
++
61
++
62
++
63
++
64
++
65
++
66
++
67
++
68
++
69
++
70
++
71
++
72
++
73
++
74
++
75
++
76
++
77
++
78
++
79
**
82
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
++
36
++
37
++
38
++
39
++
40
++
41
++
42
++
43
++
44
++
45
++
46
++
47
++
48
++
49
++
50
++
51
++
52
++
53
++
54
++
55
++
56
++
57
++
58
++
59
++
60
++
61
++
62
++
63
++
64
++
65
++
66
++
67
++
68
++
69
++
70
++
71
++
72
++
73
++
74
++
75
++
76
++
77
++
78
++
79
++
80
++
81
**
84
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
++
36
++
37
++
38
++
39
++
40
++
41
++
42
++
43
++
44
++
45
++
46
++
47
++
48
++
49
++
50
++
51
++
52
++
53
++
54
++
55
++
56
++
57
++
58
++
59
++
60
++
61
++
62
++
63
++
64
++
65
++
66
++
67
++
68
++
69
++
70
++
71
++
72
++
73
++
74
++
75
++
76
++
77
++
78
++
79
++
80
++
81
++
82
++
83
**
86
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
++
36
++
37
++
38
++
39
++
40
++
41
++
42
++
43
++
44
++
45
++
46
++
47
++
48
++
49
++
50
++
51
++
52
++
53
++
54
++
55
++
56
++
57
++
58
++
59
++
60
++
61
++
62
++
63
++
64
++
65
++
66
++
67
++
68
++
69
++
70
++
71
++
72
++
73
++
74
++
75
++
76
++
77
++
78
++
79
++
80
++
81
++
82
++
83
++
84
++
85
**
88
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
++
36
++
37
++
38
++
39
++
40
++
41
++
42
++
43
++
44
++
45
++
46
++
47
++
48
++
49
++
50
++
51
++
52
++
53
++
54
++
55
++
56
++
57
++
58
++
59
++
60
++
61
++
62
++
63
++
64
++
65
++
66
++
67
++
68
++
69
++
70
++
71
++
72
++
73
++
74
++
75
++
76
++
77
++
78
++
79
++
80
++
81
++
82
++
83
++
84
++
85
++
86
++
87
**
90
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
++
36
++
37
++
38
++
39
++
40
++
41
++
42
++
43
++
44
++
45
++
46
++
47
++
48
++
49
++
50
++
51
++
52
++
53
++
54
++
55
++
56
++
57
++
58
++
59
++
60
++
61
++
62
++
63
++
64
++
65
++
66
++
67
++
68
++
69
++
70
++
71
++
72
++
73
++
74
++
75
++
76
++
77
++
78
++
79
++
80
++
81
++
82
++
83
++
84
++
85
++
86
++
87
++
88
++
89
**
92
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
++
36
++
37
++
38
++
39
++
40
++
41
++
42
++
43
++
44
++
45
++
46
++
47
++
48
++
49
++
50
++
51
++
52
++
53
++
54
++
55
++
56
++
57
++
58
++
59
++
60
++
61
++
62
++
63
++
64
++
65
++
66
++
67
++
68
++
69
++
70
++
71
++
72
++
73
++
74
++
75
++
76
++
77
++
78
++
79
++
80
++
81
++
82
++
83
++
84
++
85
++
86
++
87
++
88
++
89
++
90
++
91
**
94
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
++
36
++
37
++
38
++
39
++
40
++
41
++
42
++
43
++
44
++
45
++
46
++
47
++
48
++
49
++
50
++
51
++
52
++
53
++
54
++
55
++
56
++
57
++
58
++
59
++
60
++
61
++
62
++
63
++
64
++
65
++
66
++
67
++
68
++
69
++
70
++
71
++
72
++
73
++
74
++
75
++
76
++
77
++
78
++
79
++
80
++
81
++
82
++
83
++
84
++
85
++
86
++
87
++
88
++
89
++
90
++
91
++
92
++
93
**
96
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
++
36
++
37
++
38
++
39
++
40
++
41
++
42
++
43
++
44
++
45
++
46
++
47
++
48
++
49
++
50
++
51
++
52
++
53
++
54
++
55
++
56
++
57
++
58
++
59
++
60
++
61
++
62
++
63
++
64
++
65
++
66
++
67
++
68
++
69
++
70
++
71
++
72
++
73
++
74
++
75
++
76
++
77
++
78
++
79
++
80
++
81
++
82
++
83
++
84
++
85
++
86
++
87
++
88
++
89
++
90
++
91
++
92
++
93
++
94
++
95
**
98
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
++
9
++
10
++
11
++
12
++
13
++
14
++
15
++
16
++
17
++
18
++
19
++
20
++
21
++
22
++
23
++
24
++
25
++
26
++
27
++
28
++
29
++
30
++
31
++
32
++
33
++
34
++
35
++
36
++
37
++
38
++
39
++
40
++
41
++
42
++
43
++
44
++
45
++
46
++
47
++
48
++
49
++
50
++
51
++
52
++
53
++
54
++
55
++
56
++
57
++
58
++
59
++
60
++
61
++
62
++
63
++
64
++
65
++
66
++
67
++
68
++
69
++
70
++
71
++
72
++
73
++
74
++
75
++
76
++
77
++
78
++
79
++
80
++
81
++
82
++
83
++
84
++
85
++
86
++
87
++
88
++
89
++
90
++
91
++
92
++
93
++
94
++
95
++
96
++
97
for i in range(10):
    if (i%2==0):
        print("**")
        print(i)
        for x in range(i):
            print("++")
            print(x)

            
**
0
**
2
++
0
++
1
**
4
++
0
++
1
++
2
++
3
**
6
++
0
++
1
++
2
++
3
++
4
++
5
**
8
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
for i in range(10):
    if (i%2==0):
        print("**")
        print(i)
        for x in range(i):
            print("|t")
            print(x)

            
**
0
**
2
|t
0
|t
1
**
4
|t
0
|t
1
|t
2
|t
3
**
6
|t
0
|t
1
|t
2
|t
3
|t
4
|t
5
**
8
|t
0
|t
1
|t
2
|t
3
|t
4
|t
5
|t
6
|t
7
for i in range(10):
    if (i%2==0):
        print("**")
        print(i)
        for x in range(i):
            print("\t")
            print(x)

            
**
0
**
2
	
0
	
1
**
4
	
0
	
1
	
2
	
3
**
6
	
0
	
1
	
2
	
3
	
4
	
5
**
8
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
for i in range(10):
    if (i%2==0):
        print("**")
        print(i)
        #for x in range(i):
         #   print("\t")
          #  print(x)

          
**
0
**
2
**
4
**
6
**
8
for i in range(10):
    #if (i%2==0):
     #   print("**")
      #  print(i)
        for x in range(i):
            print("\t")
            print(x)

            
	
0
	
0
	
1
	
0
	
1
	
2
	
0
	
1
	
2
	
3
	
0
	
1
	
2
	
3
	
4
	
0
	
1
	
2
	
3
	
4
	
5
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
for i in range(10):
    if (i%2==0):
        print("**")
        print(i)
        for x in range(i):
            print("\t")
            print(x)

            
**
0
**
2
	
0
	
1
**
4
	
0
	
1
	
2
	
3
**
6
	
0
	
1
	
2
	
3
	
4
	
5
**
8
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
for i in range(10):
    if (i%2==0):
        print("**")
        print(i)
        for x in range(i):
            print("\t")
            print(x)
    else:
        print("fail", i)

        
**
0
fail 1
**
2
	
0
	
1
fail 3
**
4
	
0
	
1
	
2
	
3
fail 5
**
6
	
0
	
1
	
2
	
3
	
4
	
5
fail 7
**
8
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
fail 9
for i in range(10):
    if (i%2==0):
        print("**", i)
        for x in range(i):
            print("\t")
            print(x)
    else:
        print("fail", i)

        
** 0
fail 1
** 2
	
0
	
1
fail 3
** 4
	
0
	
1
	
2
	
3
fail 5
** 6
	
0
	
1
	
2
	
3
	
4
	
5
fail 7
** 8
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
fail 9
for i in range(10):
    if (i%2==0):
        print("**", i)
        """for x in range(i):
            print("\t")
            print(x)
    else:"""
        print("fail", i)

        
** 0
'for x in range(i):\n            print("\t")\n            print(x)\n    else:'
fail 0
** 2
'for x in range(i):\n            print("\t")\n            print(x)\n    else:'
fail 2
** 4
'for x in range(i):\n            print("\t")\n            print(x)\n    else:'
fail 4
** 6
'for x in range(i):\n            print("\t")\n            print(x)\n    else:'
fail 6
** 8
'for x in range(i):\n            print("\t")\n            print(x)\n    else:'
fail 8
for i in range(10):
    if (i%2==0):
         print("**", i)
    else:
        print("fail", i)

        
** 0
fail 1
** 2
fail 3
** 4
fail 5
** 6
fail 7
** 8
fail 9
for i in range(10):
    if (i%2==0):
         print("**", i)
         for x in range(i):
            print("\t")
            print(x)
    else:
        print("fail", i)

        
** 0
fail 1
** 2
	
0
	
1
fail 3
** 4
	
0
	
1
	
2
	
3
fail 5
** 6
	
0
	
1
	
2
	
3
	
4
	
5
fail 7
** 8
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
fail 9
for num in range(1,101):
    if(num%==0):
        
SyntaxError: invalid syntax
for num in range(1,101):
    if(num%2==0):
        print("even")
    else:
        print("odd")

        
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
for num in range(1,101):
    if(num%2==0):
        print("even", i)
    else:
        print("odd", i)

        
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
odd 9
even 9
for num in range(1,101):
    if(num%2==0):
        print("even", num)
    else:
        print("odd", num)

        
odd 1
even 2
odd 3
even 4
odd 5
even 6
odd 7
even 8
odd 9
even 10
odd 11
even 12
odd 13
even 14
odd 15
even 16
odd 17
even 18
odd 19
even 20
odd 21
even 22
odd 23
even 24
odd 25
even 26
odd 27
even 28
odd 29
even 30
odd 31
even 32
odd 33
even 34
odd 35
even 36
odd 37
even 38
odd 39
even 40
odd 41
even 42
odd 43
even 44
odd 45
even 46
odd 47
even 48
odd 49
even 50
odd 51
even 52
odd 53
even 54
odd 55
even 56
odd 57
even 58
odd 59
even 60
odd 61
even 62
odd 63
even 64
odd 65
even 66
odd 67
even 68
odd 69
even 70
odd 71
even 72
odd 73
even 74
odd 75
even 76
odd 77
even 78
odd 79
even 80
odd 81
even 82
odd 83
even 84
odd 85
even 86
odd 87
even 88
odd 89
even 90
odd 91
even 92
odd 93
even 94
odd 95
even 96
odd 97
even 98
odd 99
even 100
for num in range(1,101):
    if(num%2==0):
        print(num, "even")
    else:
        print(num, "odd")

        
1 odd
2 even
3 odd
4 even
5 odd
6 even
7 odd
8 even
9 odd
10 even
11 odd
12 even
13 odd
14 even
15 odd
16 even
17 odd
18 even
19 odd
20 even
21 odd
22 even
23 odd
24 even
25 odd
26 even
27 odd
28 even
29 odd
30 even
31 odd
32 even
33 odd
34 even
35 odd
36 even
37 odd
38 even
39 odd
40 even
41 odd
42 even
43 odd
44 even
45 odd
46 even
47 odd
48 even
49 odd
50 even
51 odd
52 even
53 odd
54 even
55 odd
56 even
57 odd
58 even
59 odd
60 even
61 odd
62 even
63 odd
64 even
65 odd
66 even
67 odd
68 even
69 odd
70 even
71 odd
72 even
73 odd
74 even
75 odd
76 even
77 odd
78 even
79 odd
80 even
81 odd
82 even
83 odd
84 even
85 odd
86 even
87 odd
88 even
89 odd
90 even
91 odd
92 even
93 odd
94 even
95 odd
96 even
97 odd
98 even
99 odd
100 even
for num in range(1,101):
    if(num%2==0):
    else:
        print(num, "odd")
        
SyntaxError: expected an indented block after 'if' statement on line 2
for num in range(1,101):
    if(num%2==0):
        print( )
    else:
        print(num, "odd")

        
1 odd

3 odd

5 odd

7 odd

9 odd

11 odd

13 odd

15 odd

17 odd

19 odd

21 odd

23 odd

25 odd

27 odd

29 odd

31 odd

33 odd

35 odd

37 odd

39 odd

41 odd

43 odd

45 odd

47 odd

49 odd

51 odd

53 odd

55 odd

57 odd

59 odd

61 odd

63 odd

65 odd

67 odd

69 odd

71 odd

73 odd

75 odd

77 odd

79 odd

81 odd

83 odd

85 odd

87 odd

89 odd

91 odd

93 odd

95 odd

97 odd

99 odd

for num in range(1,101):
    if(num%2==0):
        print()
    else:
        print(num, "odd")

        
1 odd

3 odd

5 odd

7 odd

9 odd

11 odd

13 odd

15 odd

17 odd

19 odd

21 odd

23 odd

25 odd

27 odd

29 odd

31 odd

33 odd

35 odd

37 odd

39 odd

41 odd

43 odd

45 odd

47 odd

49 odd

51 odd

53 odd

55 odd

57 odd

59 odd

61 odd

63 odd

65 odd

67 odd

69 odd

71 odd

73 odd

75 odd

77 odd

79 odd

81 odd

83 odd

85 odd

87 odd

89 odd

91 odd

93 odd

95 odd

97 odd

99 odd

for num in range(1,101):
    if(num%2!=0):
        print(num, "odd")

        
1 odd
3 odd
5 odd
7 odd
9 odd
11 odd
13 odd
15 odd
17 odd
19 odd
21 odd
23 odd
25 odd
27 odd
29 odd
31 odd
33 odd
35 odd
37 odd
39 odd
41 odd
43 odd
45 odd
47 odd
49 odd
51 odd
53 odd
55 odd
57 odd
59 odd
61 odd
63 odd
65 odd
67 odd
69 odd
71 odd
73 odd
75 odd
77 odd
79 odd
81 odd
83 odd
85 odd
87 odd
89 odd
91 odd
93 odd
95 odd
97 odd
99 odd
for num not in range(1,101):
    if(num%2!=0):
        print(num, "odd")
        
SyntaxError: invalid syntax

for num in range(1,101):
    if(num%3!=0):
        print(num, "odd")

        
1 odd
2 odd
4 odd
5 odd
7 odd
8 odd
10 odd
11 odd
13 odd
14 odd
16 odd
17 odd
19 odd
20 odd
22 odd
23 odd
25 odd
26 odd
28 odd
29 odd
31 odd
32 odd
34 odd
35 odd
37 odd
38 odd
40 odd
41 odd
43 odd
44 odd
46 odd
47 odd
49 odd
50 odd
52 odd
53 odd
55 odd
56 odd
58 odd
59 odd
61 odd
62 odd
64 odd
65 odd
67 odd
68 odd
70 odd
71 odd
73 odd
74 odd
76 odd
77 odd
79 odd
80 odd
82 odd
83 odd
85 odd
86 odd
88 odd
89 odd
91 odd
92 odd
94 odd
95 odd
97 odd
98 odd
100 odd
for num in range(1,101):
    if(num%3==0):
        print(num, "--multiple of 3")

        
3 --multiple of 3
6 --multiple of 3
9 --multiple of 3
12 --multiple of 3
15 --multiple of 3
18 --multiple of 3
21 --multiple of 3
24 --multiple of 3
27 --multiple of 3
30 --multiple of 3
33 --multiple of 3
36 --multiple of 3
39 --multiple of 3
42 --multiple of 3
45 --multiple of 3
48 --multiple of 3
51 --multiple of 3
54 --multiple of 3
57 --multiple of 3
60 --multiple of 3
63 --multiple of 3
66 --multiple of 3
69 --multiple of 3
72 --multiple of 3
75 --multiple of 3
78 --multiple of 3
81 --multiple of 3
84 --multiple of 3
87 --multiple of 3
90 --multiple of 3
93 --multiple of 3
96 --multiple of 3
99 --multiple of 3
for num in range(1,101):
    if(num%6==0):
        print(num, "--multiple of 6")

        
6 --multiple of 6
12 --multiple of 6
18 --multiple of 6
24 --multiple of 6
30 --multiple of 6
36 --multiple of 6
42 --multiple of 6
48 --multiple of 6
54 --multiple of 6
60 --multiple of 6
66 --multiple of 6
72 --multiple of 6
78 --multiple of 6
84 --multiple of 6
90 --multiple of 6
96 --multiple of 6
range(10)
range(0, 10)
print(range(10))
range(0, 10)
help(range)
Help on class range in module builtins:

class range(object)
 |  range(stop) -> range object
 |  range(start, stop[, step]) -> range object
 |  
 |  Return an object that produces a sequence of integers from start (inclusive)
 |  to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
 |  start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
 |  These are exactly the valid indices for a list of 4 elements.
 |  When step is given, it specifies the increment (or decrement).
 |  
 |  Methods defined here:
 |  
 |  __bool__(self, /)
 |      True if self else False
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __reduce__(...)
 |      Helper for pickle.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      Return a reverse iterator.
 |  
 |  count(...)
 |      rangeobject.count(value) -> integer -- return number of occurrences of value
 |  
 |  index(...)
 |      rangeobject.index(value) -> integer -- return index of value.
 |      Raise ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  start
 |  
 |  step
 |  
 |  stop

[range(10)]
[range(0, 10)]
print([range(10)])
[range(0, 10)]
list(range(20))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
list(for num in range(20):)
SyntaxError: invalid syntax
list(range(0,10,2))
[0, 2, 4, 6, 8]
list(range(1,10,2))
[1, 3, 5, 7, 9]
list(range(3,10,3))
[3, 6, 9]
list(range(1,100,2))
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
list(range(10,101,10))
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list(range(0,100,2))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
list(range(2,100,2))
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
list(range(1,100,2))
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
list(range(2,101,2))
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
nums = [1,3,4,6,7,3,7,6,5,12,54,2,3]
dir(nums)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
type(nums)
<class 'list'>
for x in nums:
    print(x)

    
1
3
4
6
7
3
7
6
5
12
54
2
3
nums = [1,3,4,6,7,3,7,6,5,12,54,2,3,ui, afyu,uu, 88, fs3,0k]
SyntaxError: invalid decimal literal
nums = [1,3,4,6,7,3,7,6,5,12,54,2,3,ui, afyu,uu, 88, fs3,ok]
Traceback (most recent call last):
  File "<pyshell#289>", line 1, in <module>
    nums = [1,3,4,6,7,3,7,6,5,12,54,2,3,ui, afyu,uu, 88, fs3,ok]
NameError: name 'ui' is not defined. Did you mean: 'u'?
nums = [1,3,4,6,7,3,7,6,5,12,54,2,3,"ui", "afyu","uu", 88,"fs3","ok"]
for c in nums:
    print(c)

    
1
3
4
6
7
3
7
6
5
12
54
2
3
ui
afyu
uu
88
fs3
ok
>>> len(nums)
19
>>> for c in nums:
...     print(0)
... 
...     
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
>>> nums[0]
1
>>> nums[-1]
'ok'
