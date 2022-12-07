"""def hello():
    this function shows hello and you can get a warm morning hello from here.
this is very
useful
    print("hi")

hello()
print("I am here.")
print(hello.__name__)
#print(hello.__doc__) #use this function as message in program to give examples too.


def add(a,b=1): #b=1 is a default parameter
    x=a+b
    print("total =",x)
   
add(2,3)
add(3)
add(6,10)"""

"""def add(a=0,b=0):
    
    if a>=0 and b>=0: #for int
        total = a+b
    if a==' ' or b==' ': # for empty
        total=0
    total=a+b
    print(total)
    return total

add(10,20)
add()
add(10)"""



"""def add(a,b=0):
    if a>0:
        total=a+b
        print(total)
        return total
    if a<=0:
        total="wrong value"
        print(total)
        return total   #in multiple condition every step return makes process fast
    
add(-10)
add(0)
add(10,33)
add(-1,7)"""



def add(*a):
   
    """print(type(a))
    new = list(a)
    print(new)
    print(type(new))"""

    return sum(a)
    
print(add())
print(add(1,2,3))
print(add(1))
print(add("apple",32 , "aa"))






        
    
        


