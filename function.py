# function -> set of action to be performed

# function creation

# def funcyion_name():
    # statement

# function calling

# funcyion_name()


def add():
    a = 10
    b = 5
    c = a+b
    print(c)

add()

# without argument

def say():
    print("Hello");
say()

# with argument

def add(a,b):
    c = a+b
    print(c)
add(10,5)

def say(name):
    print("My name is",name)
say("Abi")

# without return

def square():
    a = 10
    print(a*a)

square()

# with return

def square():
    a = 10
    return  a*a

print(square())

res = square()
print(res)


def square(a):
    return a*a
print(square(10))
print(square(5))
print(square(3))
print(square(12))


# Function with multiple return type

def calc(a,b):
    sum = a+b
    sub = a-b
    mul = a*b
    div = a/b

    return sum , sub, mul, div
print(calc(10,5))
print(type(calc(10,5)))
for i in calc(100,50):
    print(i)

result = calc(10,4)
for i in result:
    print(i)

i,j,k,l = calc(10,5)
print(l)
print(j)


def calc(a,b):
    sum = a + b
    sub = a - b
    mul = a * b
    div = a / b

    print(sum)
    print(sub)
    print(mul)
    print(div)


# function with multiple variable argument length

def add(*a):
    print(a)
add(10,5)

# l = [1,2,3,4,5]

def add(*a):
    sum = 0
    for i in a:
        sum +=i
    print(sum)

add(10,40,50,30,20,70)


def add(*a):
    sum = 0
    for i in a:
        sum+=i # sum = sum +i
    return sum

print(add(10,20,30,40,50))

# Function with keyword argument

def mydetails(age , name):
    print("My age is",age, "My name is",name)

mydetails(20,"Mano")
mydetails("mano",20)

mydetails(age = 20,name = "Mano")
mydetails(name="Mano", age = 20)

# Function with default keyword argument

def mydetails(age=10,name="Abi"):
    print("My age is",age)
    print("My name is",name)
mydetails()
mydetails(20)
mydetails("Barath")
mydetails(age =30)
mydetails(name = "Sai")
mydetails(age = 15, name = "Alan")

# Function with multiple variable keyword argument

def mydetails(**details):
    print(details)
    print(type(details))
    for k,v in details.items():
        # print(k)
        # print(v)
        print(k,"-",v)
mydetails(age = 20)
mydetails(age = 20, name = "Abi")
mydetails(age = 20, name = "Abi", heigth= 170, rollno= 12334)


# types of variable
# local - with in function
# global - variable outside function also access

# local

def add():
    a = 10
    print(a)

def sub():
    b = 20
    print(b)
    # print(a)

add()
sub()

# global - declare outside the function  call also outside and inside the function

c = 100
def add():
    a = 10
    print(a)
    print(c)

def sub():
    b = 20
    print(b)
    print(c)

print(c)
add()
sub()


a = 100 # global variable
def add():
    a = 10 # local variable
    print(a)
    print(globals()["a"])
    print(globals().get("a"))

add()

# local to global

def add():
    a = 100
    global d
    d = 400
    print(a)

def sub():
    b = 200
    print(b)
    print(d)

add()
sub()

# Recursive function --> function call own itself

def fun():
    print("hello")
fun()

def fun():
    for i in range(1,11,1):
        print("hello")
fun()

print("_______________________________")
count  = 0
def fun():
    global count
    print("hello", count+1)
    count = count+1
    if count<10:
        fun()
fun()

print("------------------------------")

def fun(num):
    if num==0:
        return
    print(num)
    fun(num-1)
fun(5)

# f(n) num==0 ret  p(n)  f(n-1)
#   5  5==0          5    5-1=4
#   4  4==0          4    4-1=3
#   3  3==0          3    3-1=2
#   2  2==0          2    2-1=1
#   1  1==0          1    1-1=0
#   0  0==0----------------------------


def fun(num):
    if num==6:
        return
    print(num)
    fun(num+1)
fun(1)

print("------------------------------")

def fun(num):
    if num==0:
        return
    fun(num-1)
    print(num)

fun(5)
fun(10)
fun(100)

# fun(num) num==0 retrun fun(num-1) print(num)
#      5    5==0          5-1=4       5?
#      4    4==0          4-1=3       4?
#      3    3==0          3-1=2       3?
#      2    2==0          2-1=1       2?
#      1    1==0          1-1=0       1?
#      0    0==0-----------------