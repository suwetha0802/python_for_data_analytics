#while loop

#Syntax
#while(condition):
#loop

#Print numbers from 1 to 5

i=1
while i<=5:
    print(i)

#Print numbers from 5 to 1

i=5
while i>=1:
    print(i)

#Print even numbers

i=1
while i<=10:
    if i%2==0:
        print(i)
    i+=1

#Print numbers divisible by 2 and 3 and 5

i=1
while i<=100:
    if i%2==0 and i%3==0 and i%5==0:
        print(i)
    i+=1

#Print a word in reverse

word="Towel"
rev=""
i=len(word)-1
while i>=0:
    rev=rev+word[i]
    i-=1
print(rev)

#Check whether the given word is palindrome or not

word="mam"
rev=""
i=len(word)-1
while i>=0:
    rev=rev+word[i]
    i-=1
print(rev)
if rev==word:
    print("Its Palindrome")
else:
    print("Its not a palindrome")

#Find the sum of first 10 natural numbers

sum=0
i=1
while i<=10:
    sum=sum+i
    i+=1
print("Sum is:",sum)

#Print the multiplication table of a given number

i=1
while i<=10:
    print(i,"* 4 =",i*4)
    i+=1

#Find the factorial of a number

fact=1
i=1
while i<=5:
    fact=fact*i
    i+=1
print("Factorial is:",fact)

#Count the number of digits in a given number

n=int(input("Enter a number:"))
count=0
while n>0:
    count=count+1
    n=n // 10
print("Number of digits:",count)

#Print all prime numbers between 1 to 50

num=1
while num<=5:
    if num>1:
        i = 2
        while i<num:
            if num%i == 0:
                break
            i+=1
        else:
            print(num)
    num+=1

#Generate fibonacci series

n=int(input("Enter a number:"))
a=0
b=1
i=0
while i<=n:
    print(a)
    c=a+b
    a=b
    b=c
    i+=1

#Create a simple logic system(3 attempts only)

password="suwetha" 
attempts=0
while attempts<=3:
    user=input("Enter password:")
    if user==password:
        print("Login Successful")
    else:
        print("Wrong Password")
    attempts+=1
    if attempts==3:
        print("Account Locked")

#Keep asking until user enters 0

num=1
while num!=0:
    num=int(input("Enter a number:"))
    print("You entered")
    