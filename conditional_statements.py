#if

#Syntax:
#if(condition):
   #statement

#Example:
mark=68
if(mark>=35):
 print("Pass")

#if 

#Syntax:
#if (condition):
   #statement 1
#else:
   #statement 2

#Example:1
mark=20
if(mark>=35):
  print("Pass")
else:
  print("Fail")

#Example:2
n=15
if(n%2==0):
    print("Even")
else:
    print("Odd")

#Example:3
num=-15
if(num>0):
    print("Positive")
else:
    print("Negative")

#Logical AND

#Example:1
a=10
b=18
c=5
if((a>b)and (a>c)):
    print("a is greater")
else:
    print("a is not greater")

#Example:2

age=20
weight=65
if(age>18 and weight>60):
    print("able to donate ")
else:
    print("not able to donate blood")

#Logical OR

#Example:
age=3
height=90
if(age<=4 or height<=100):
    print("Half ticket")
else:
    print("Full ticket")

#elif

#Syntax:
#if(condition):
  #statement
#elif(condition)
   #statement
#….
#….
#….
#else:
  #statement

#Example:
mark=-123
if(mark<100 and mark>=90):
    print("grade A")
elif(mark<90 and mark>=80):
    print("grade B")
elif(mark<80 and mark>=70):
    print("grade c")
elif(mark<70 and mark>=60):
    print("grade d")
elif(mark<60 and mark>=50):
    print("grade e")
elif(mark<50 and mark>=0):
    print("Fail")
else:
    print("Invalid Mark")

#Nested if

#Syntax:
#if(condition):
  #if(condition):

#Examble:
n=int(input("Enter a number:"))
if(n>0):
    print("The number is positive")
    if(n%2==0):
        print("The number is even")
    else:
        print("The number is odd")
elif(n<0):
    print("The number is negative")
    if(n%2==0):
         print("The number is even")
    else:
        print("The number is odd")
else:
    print("The number is zero")
    
















        