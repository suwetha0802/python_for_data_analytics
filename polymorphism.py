# POLYMORPHISM
# one name , many forms

# The same method name can perform different action for different object
# Its allows the same method name to work with different object
# Mainly achived using method overriding in inheritance
# Improves code reusability and flexibility

# Python supports polymorphism in:
    # Function
    # operators
    # class methods

# operator overloading

#Example:1

a = 10
b = 5
print(a+b)

#Example:2

a = "Ma"
b = "no"
print(a+b)

# function overloading

#Example:1

def add(a,b):
    return a+b
print(add(2,3))
# print(add(3))

#Example:2

def add(a=0,b=0):
    return a+b
print(add(2))
print(add(b=2))
print(add(a = 3, b = 4))


# Method overloading - multiple methods with same name but different parameters in the same class

class Employee():
    def employee_details(self,id):
        print("Employee id is ",id)
    def employee_details(self,name):
        print("Employee name is ",name)
    def employee_details(self,id=None, name=None):
        print("Employee id is ",id )
        print("Employee name is ",name)

e= Employee()
e.employee_details(13255)
e.employee_details(name = "Mano")
e.employee_details(124325,"Sai")
e.employee_details("Sai",23443546)
e.employee_details(name ="Sai",id =23443546)

# Method overriding - Child class provides its own implementation of a method already define in parent class

#Example:1

class Employee():
    def employee_id(self,id):
        print("Employee id is ",id)
    def employee_name(self,name):
        print("Employee name is ",name)

class Employee1(Employee):
    def employee_id(self,id):
        print("Employee 1 id is ",id)
    def employee_name(self,name):
        print("Employee 1 name is ",name)

e = Employee1()
e.employee_id(12344)
e.employee_name("Abi")

#Example:2

class RBI():
    def saving(self):
        print("Saving 6%")
    def current(self):
        print("Current 7%")
    def fixed(self):
        print("Fixed 9%")

class SBI(RBI):
    def saving(self):
        print("Saving 7%")
    def current(self):
        print("Current 8%")
    def deposit(self):
        print("Deposit 5%")

s = SBI()
s.saving()
s.current()
s.deposit()
s.fixed()

#Example:3

class Shape():
    def area(self,dim1,dim2):
        pass

class Aree(Shape):
    def area(self):
        print("Find the area")

class Rectangle(Shape):
    def area(self,len,br):
        print("Area of rectangle is ",len*br)

class Square(Shape):
    def area(self,side):
        print("Area of Square is ",side*side)

a = Aree()
a.area()

r = Rectangle()
r.area(10,4)

s =Square()
s.area(10)