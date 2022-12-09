#Array: Collection/container -> DataType Same! : String!
#Iterate: move on indexwise/element side..List,Tuple,Dict,Set
#(String can be use as Iterator!)
#Mutable: Index base -> update (List!)  (neg: Immutable! -> String)

varList = [12,34,67,89,0,1,2,3,4]

def normalFunction():
    result = []
    for var in varList:
        result.append(var)
    return result

print("MainList: ",varList)

print("Normal Function TEST")
value = normalFunction()
print(type(value))
print(value)


#every generator is an Iterator, but not Vice Versa.
#Uses 'yield' keyword and return an Iterator
def generatorFunction():
    for x in varList:
        yield x+2 #14,36,...6

    #create: temp array
    #append to temp array
    #finally: return (temp array)

#generator is where yield is used instead of return

print("\n\nYield Generator Test")
print(type(generatorFunction()))
valuey = list(generatorFunction())
print(valuey)


def check():
    yield 10
    yield 20
    yield "python"

print(list(check)())
