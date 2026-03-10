#INHERITANCE

# Child class to use properties and method of a parent class
# It helps in code reusability and reduce duplication
# parent - base or super class
# child - derived or sub class
# Use parent class name inside brackets while creating the child class

# class ParentClass():

# class ChildName(ParentClass):

class Details():
    def details(self,name,age):
        self.n= name
        self.a = age

class Display(Details):
    def display(self):
        print(self.n)
        print(self.a)

d = Display()
d.details("Sai",23)
d.display()

#1.Single Inheritance

print("--------Single inheritance-----------")

class Employee():
    def employee_name(self):
        print("Employee name is Mano")
    def employee_id(self):
        print("Employee id is 436575")

class Company(Employee):
    def company_name(self):
        print("Company name is CTS")
    def company_id(self):
        print("Company id is 98742")

c = Company()
c.company_name()
c.company_id()
c.employee_name()
c.employee_name()

#2. Multilevel -- tree level

print("----------Multilevel inheritance--------")

class Employee():
    def employee_name(self):
        print("Employee name is Mano")
    def employee_id(self):
        print("Employee id is 436575")

class Company(Employee):
    def company_name(self):
        print("Company name is CTS")
    def company_id(self):
        print("Company id is 98742")
class Client(Company):
    def client_name(self):
        print("Client name is Amazon")
    def client_id(self):
        print("Client id is 243512")

cl = Client()
cl.client_name()
cl.client_id()
cl.company_name()
cl.company_id()
cl.employee_name()
cl.employee_id()

#3. multiple -- parallel level

print("----------Multiple Inheritance-----------")

class Employee():
    def employee_name(self):
        print("Employee name is Mano")
    def employee_id(self):
        print("Employee id is 436575")
    def details(self):
        print("Employee details")

class Company():
    def company_name(self):
        print("Company name is CTS")
    def company_id(self):
        print("Company id is 98742")
    def details(self):
        print("Company details")

class Client(Employee,Company):
    def client_name(self):
        print("Client name is Amazon")
    def client_id(self):
        print("Client id is 243512")
    def details(self):
        print("Client details")

cl = Client()
cl.client_name()
cl.client_id()
cl.company_name()
cl.company_id()
cl.employee_name()
cl.employee_id()
cl.details()

#4. Hierarchical Inheritance

print("---------Hierarchical inheritance---------")

class Employee():
    def employee_name(self):
        print("Employee name is Mano")
    def employee_id(self):
        print("Employee id is 436575")
    def details(self):
        print("Employee details")

class Company(Employee):
    def company_name(self):
        print("Company name is CTS")
    def company_id(self):
        print("Company id is 98742")
    def details(self):
        print("Company details")

class Client(Employee):
    def client_name(self):
        print("Client name is Amazon")
    def client_id(self):
        print("Client id is 243512")
    def details(self):
        print("Client details")

co = Company()
co.company_name()
co.company_id()
co.employee_name()
co.employee_id()
co.details()

cl = Client()
cl.client_name()
cl.client_id()
cl.employee_name()
cl.employee_id()
cl.details()

