# Anonymous function


# lambda - A lambda in python is a small anonymous function used for short simple operation

# varName = lambda argument:action

def add(a,b):
    return a+b
print(add(10,4))

lam = lambda a,b:a+b
print(lam(10,3))

def isEven(num):
    return num%2==0
print(isEven(10))
print(isEven(11))

isEven = lambda num : num%2==0
print(isEven(10))
print(isEven(21))

# Filter
# This not perform any action it just filter the values based on condition
# it return only true
# output size mey be equal or below
# filter accepts tow parameters

# filter(function, iterable values)

l = [1,2,3,4,5,6,7,8]
l2 = []

for i in l:
    if i%2==0:
        l2.append(i)
print(l2)

def iseven(num):
    return num%2==0

# with filter

l = [1,2,3,4,5,6,7,8]
def isEven(num):
    return num%2==0

print(list(filter(iseven,l)))

# with lambda
l = [1,2,3,4,5,6,7,8]
print(list(filter(lambda a:a%2==0, l)))

# Map
# This will perform action based on condition
# output size equal to input
# map accepts two parameters

# map(function, iterable value)

l = [1,2,3,4]
l2 = []

for i in l:
    sq = i*i
    l2.append(sq)
print(l2)

def squareRoot(num):
    return num*num
print(squareRoot(5))

# With map
l = [1,2,3,4,5]
def square(num):
    return num*num
print(list(map(square,l)))

# with lambda
l = [5,6,7,8]
print(list(map(lambda a:a*a, l)))
print(list(map(lambda a:a*a, [1,2,3,4,5])))

# reduce
# This will perform action based on caondition
# output size only one
# reduce accepts tow parameters

# reduce(function, iterable values)

l = [1,2,3,4,5]
sum = 0
for i in l:
    sum = sum+i
print(sum)

def add(a,b):
    return a+b

# with reduce
from functools import reduce
l = [10,20,30,40,50]
print(reduce(add,l))

# with lambda
l = [100,200,300,400,500]
print(reduce(lambda a,b:a+b, l))