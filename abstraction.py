# ABSTRACTION 
# - Hiding the implementation or business logics of method

from abc import ABC,abstractmethod

#Example:1

class Rbi(ABC):
    @abstractmethod
    def saving(self):
        pass
    @abstractmethod
    def current(self):
        pass

    def fixed(self):
        print("fixed 7%")

class Sbi(Rbi):
    def saving(self):
        print("Saving 4%")

    def current(self):
        print("Current")

    def deposit(self):
        print("Deposit 6%")

s = Sbi()
s.saving()
s.current()
s.deposit()
s.fixed()

#Example:2

class Bank(ABC):
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
    @abstractmethod
    def balance(self):
        pass

class Sbi(Bank):
    def __init__(self):
        self.bal = 15000

    def deposit(self,amount):
        if amount>0:
            self.bal+=amount
            print("Deposit Amount :",amount)
        else:
            print("Deposit a valid amount")

    def withdraw(self,amount):
        if amount<=self.bal:
            self.bal-=amount
            print("Withdraw amount :",amount)
        else:
            print("Withdraw a valid amount")

    def balance(self):
        print("Balance Amount :",self.bal)

s = Sbi()
print("SBI BANK")
s.deposit(10000)
s.withdraw(8000)
s.balance()
