"""
Class: callable __call__
"""

class A:
    """Class A, displaying Arguments"""

    def __init__(self):
        print("An instance of A was initialized")

    def __del__(self):
        print("an instance of A will be deleted")
    
    def __call__(self, *args, **kwargs):
        print("Arguments are:", args, kwargs)
              
print(A.__doc__)
x = A() #creating Object x
b = A() #creating Object b
d = A() #creating Object d
print(x.__doc__)

print("\nCalling the instance:")
x(3, 4, x=11, y=10)
b(44,32,1,t=23 ,f=1)

print("Let's call it again:")
x(3, 4,8, x=11, y=10,u=85)

del x
del b
del d
