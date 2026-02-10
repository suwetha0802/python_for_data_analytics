#for loop

#Write a program to print numbers from 1 to 10 using a for loop.
for i in range(1,11,1):
    print(i)

#Print all even numbers between 1 and 20
for i in range(1,20):
    if(i%2==0):
        print(i)

for i in range(0,20,2):
    print(i)

#Find the sum of first 10 natural numbers using a for loop.
sum=0
for i in range(1,11):
    sum=sum+i
print(sum)

#Print the multiplication table of a given number (for example, 5).
for i in range(1,11):
    print(i,"* 5 =",i*5)

#Given a list [10, 20, 30, 40, 50], print each element using a for loop.
list1 = [10, 20, 30, 40, 50]
for i in list1:
    print(i)

#Write a program to count the number of vowels in a given string
text = "python"
count = 0
for i in text:
    if i in "aeiou":
        count = count + 1
print("Vowels =", count)

#Find the factorial of a number using a for loop.
fact=1
for i in range(1,6):
    fact=fact*i
print(fact)

#Reverse a given string using a for loop.
word="hello"
rev=""
for i in range(len[str]-1,-1,-1):
    rev=rev+str[i] 
print(rev)

#Print * pattern using a for loop:
for i in range(1,6):
    print("*"*i)

#Print prime numbers
for num in range(1,7):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
                print(num)
