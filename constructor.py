# CONSTRUCTOR

# Used to initialize object variables
# Called automatically
# self refers to the cutter object

# SYNTAX

# def __init__(self):

class Student():
    def student_id(self):
        print("My id is 4656")
    def __init__(self):
        print("My name is Abi")
s =Student()
s.student_id()

# TYPES OF CONSTRUCTOR

# Default or non - parameterized constructor

class Car():
    def __init__(self):
        print("Car name is Tata")
Car()

# 2. Parameterized constructor

class Student():
    def __init__(self,name,age):
        print("My name is",name)
        print("My age is",age)
Student("Mano",21)

#Example:1

class Employee():
    def __init__(self):
        print("Default constructor")
    def employee_one(self,username,password):
        print(username)
        print(password)
    def employee_two(self,username,password):
        print(username)
        print(password)

e = Employee()
e.employee_one("abi2@gmail.com",456463)
e.employee_two("barath3@gmail.com",783646)

#Example:2

class Employee():
    def __init__(self):
        print("Default constructor")
    def employee_one(self,username,password):
        self.ps = password
        print(username)
        print(password)
    def employee_two(self,username):
        print(username)
        print(self.ps)

e = Employee()
e.employee_one("abi@gmail.com",5754353)
e.employee_two("barath@gmail.com")

#Example:3

class Employee():
    def __init__(self,password):
        self.ps = password
        print("Default constructor")
    def employee_one(self,username):
        print(username)
        print(self.ps)
    def employee_two(self,username):
        print(username)
        print(self.ps)

e = Employee(67567567)
e.employee_one("abi@gmail.com")
e.employee_two("barath@gmail.com")

#Example:4

class Employee():
    def __init__(self,password):
        self.ps = password
    def employee_one(self,username):
        print(username)
        print(self.ps)
    def employee_two(self,username):
        print(username)
        print(self.ps)

e1 = Employee(67567567)
e1.employee_one("abi@gmail.com")

e2 = Employee(132345677)
e2.employee_two("barath@gmail.com")

#Example:5

class Employee():
    def __init__(self,username,password):
        self.us = username
        self.ps = password
        print("Default constructor")
    def employee_one(self):
        print(self.us)
        print(self.ps)
    def employee_two(self):
        print(self.us)
        print(self.ps)

e1 = Employee("abi@gmail.com",67567567)
e1.employee_one()

e2 = Employee("barath@gmail.com",1243453)
e2.employee_two()

#Example:6

class Area():
    def __init__(self,dim1,dim2):
        self.d1= dim1
        self.d2 = dim2

    def areaRec(self):
        print("Area of rectangle is",self.d1*self.d2)
    def areTri(self):
        print("Area of triangle is",0.5*self.d1*self.d2)

a = Area(10,5)
a.areaRec()
a.areTri()

#Example:7

class Area():
    def __init__(self,dim1,dim2):
        self.d1= dim1
        self.d2 = dim2
    def areaRec(self):
        print("Area of rectangle is",self.d1*self.d2)
    def areTri(self):
        print("Area of triangle is",0.5*self.d1*self.d2)

a1 = Area(10,5)
a1.areaRec()

a2 = Area(8,4)
a2.areTri()

#Create a class Employee with constructor to initialize id, name, salary.

class Employee():
    def __init__(self,name,id,salary):
        self.n=name
        self.i=id
        self.s=salary
        print("Employee Detais")
    def employee_details(self):
        print("Name:",self.n)
        print("ID:",self.i)
        print("Salary:",self.s)
e=Employee("Suwetha", 96 , 45000)
e.employee_details()

#Create a class Car using constructor to set brand and model.

class Car():
    def __init__(self,brand,model):
        self.b=brand
        self.m=model
        print("Car Info")
    def display(self):
        print("Car Brand:",self.b)
        print("Car Model:",self.m)
c=Car("Toyota","Corrolla")
c.display()

#Create a class Rectangle with constructor to initialize length and width and calculate area.

class Area():
    def __init__(self,length,width):
        self.l=length
        self.w=width
    def areaREC(self):
        print("Area of Rectangle is ",self.l*self.w)
a=Area(5,6)
a.areaREC()

#Create a class Laptop with constructor to initialize brand, ram, price.

class Laptop():
    def __init__(self):
        print("Laptop info")
    def details(self,brand,ram,price):
        print("Brand:",brand)
        print("RAM:",ram)
        print("Price:",price)
l=Laptop()
l.details("Lenova", "34GB" , 50000)
        
#Create a class Book with constructor to initialize title and author.

class Book():
    def __init__(self,title,author):
        self.t=title
        self.a=author
        print("Book Details")
    def book1(self):
        print("Tite:",self.t)
        print("Author:",self.a)
    def book2(self):
        print("Tite:",self.t)
        print("Author:",self.a)
b1=Book("Wings of Fire","A.P.J.Abdul Kalam")
b1.book1()

b2=Book("One life","Shakesphere")
b2.book2()
        
#Create a class Person with constructor to print name and age.

class Person():
    def __init__(self):
        print("Person Details")
    def details(self,name,age):
        print("Name:",name)
        print("Age:",age)
p=Person()
p.details("Suwetha",21)

#Create a class Product with constructor to initialize product_name and price.

class Product():
    def __init__(self,name,price):
        self.n=name
        self.p=price
    def details(self):
        print("Product_Name:",self.n)
        print("Product_Price:",self.p)
p=Product("Shamboo", 105)
p.details()