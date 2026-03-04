# Class :

# A class Blueprint or template of creating object
# It define variables and method

# Object :

# An object is a real instance of a class
# you  can create multiple objects from one class

# Method :

# A method is function defined inside a class
# it describe the behaviour of the object
# Method always use self to access object data

# class creation

# class ClassName(): () ---> Optional
class Employee():
    # def method_name(self):
    def employee_id(self):
        print("Employee id is 23446")

    def employee_name(self):
        print("Employee name is Mano")

# object creation
#  objectRefName = ClassName()
e = Employee()

# method calling
# objectRefName.method_name()
e.employee_id()
e.employee_name()

e1  = Employee()
e1.employee_id()
e1.employee_name()

#Example:1

class Employee():
    def employee_id(self):
        print("Employee id is 2345")
        print(id(self))
    def employee_name(self):
        print("Employee name is Mano")
        print(id(self))
e = Employee()
e.employee_id()
e.employee_name()
print(id(e))

#Example:2

e1  = Employee()
e1.employee_name()
e1.employee_name()
print(id(e1))

class Employee():
    def employee(self,eid):
        print("Employee id is ",eid)
    def employee_name(self,ename):
        print("Employee name is",ename)

e  = Employee()
e.employee(234)
e.employee_name("Abi")

# with argument:

class Student():
    def student_name(self,name):
        print("Name :",name)
    def student_roll(self,roll):
        print("Roll No",roll)
stu = Student()
stu.student_name("Abi")
stu.student_roll(2342)

#default keyword argument:

class Student():
    def student_name(self,name=None):
        print("Name :",name)
    def student_roll(self,roll =0):
        print("Roll No",roll)
stu = Student()
stu.student_name()
stu.student_roll()

#with return:

class Car():
    def car_details(self):
        return "Car Name : Tata"

c= Car()
print(c.car_details())

#with multiple return type:

class Calculator():
    def operation(self,num):
        square=num**2
        cube=num**3
        return square,cube
c=Calculator()
print(c.operation(3))

#with keyword argument

class Person():
    def details_name(self,name):
        print("My name is:",name)
    def details_age(self,age):
        print("My age is:",age)
    def details_salary(self,salary):
        print("My salary is:",salary)
p=Person()
p.details_name(name="Suwetha")
p.details_age(age=21)
p.details_salary(salary=25000)

#with default keyword argument

class Library():
    def book_title(self,title="Wings of Fire"):
        print("The title is:",title)
    def book_author(self,author="A.P.J.Abdul Kalam"):
        print("The author is:",author)
    def book_copy(self,copy=1):
        print("The copies are:",copy)
l=Library()
l.book_title()
l.book_author()
l.book_copy()

#with multiple variable keyword argument

class Student():
    def student_details(self,**details):
        print(details)
s=Student()
s.student_details(name="Suwetha",age=21,dept="ECE")

#with multiple variable argument length

class Marks():
    def calculate(self,*m):
        total=sum(m)
        average=total/len(m)
        print("Total Marks=",total)
        print("Average=",average)
mar=Marks()
mar.calculate(80,55,90,60,78)

#without argument

class Message():
    def display(self):
        print("Welcome to Python")
m=Message()
m.display()

#with argument

class Square():
    def sq(self,num):
        n=num**2
        print(n)
s=Square()
s.sq(4)

#with return

class Num():
    def get_number(self):
        user=int(input("Enter a number:"))
        return user
n=Num()
print(n.get_number())

#without return

class Number():
    def largest(self,a,b):
        large=max(a,b)
        print(large)
n=Number()
n.largest(5,8)