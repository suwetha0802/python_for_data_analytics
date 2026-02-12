#JUMP STATEMENT

#Write a program to print numbers from 1 to 10,but stop the loop when the number is 5 using break
 
for i in range(1,11):
    if i==5:
        break
    print(i)

#Write a program to print numbers from 1 to 10,but skip 5 using continue

for i in range(1,11):
    if i==5:
        continue
    print(i)

#Write a program to loop from 1 to 5 and use pass the number is 3

for i in range(1,6):
    if i==3:
        pass
    print(i)

#Print all the numbers from 1 to 20 but stop if the number is greater than 15

for i in range(1,21):
    if i>=15:
        break
    print(i)

#Print only odd numbers from 1 to 10 using continue

for i in range(1,11):
    if i%2==0:
        continue
    print(i)

#Take numbers from the user in a loop and stop when the user enters 0

while True:
     num=int(input("Enter a number:"))
     if num==0:
         print("Loop stopped")
         break
     else:
         print("You entered",num)


#Print all numbers from 1 to 10,but skip multiples of 5

for i in range(1,51):
    if i%5==0:
        continue
    print(i)

#Find the first multiples of 7 btw 1 and 100 using 100

for i in range(1,101):
    if i%7==0:
        print("First multiple of 7 is:",i)
        break
    
#Write a program to check a list of numbers and stop when a negative number is found

ist=[5,10,15,-4,22]
for num in list:
    if num<0:
        print("Negative number found",num)
        break
    else:
        print("Checked number",num)

#Print characters of a string but skip vowels using continue

text="suwetha"
vowels="aeiou"
for i in text:
    if i in vowels:
        continue
    print(i)

#Create a login system

password = "suwetha"
attempts = 0
while attempts < 3:
    user = input("Enter password: ")
    if user == password:
        print("Correct password")
        break
    else:
        print("Try again")
        attempts += 1
if attempts == 3:
    print("Too many attempts. Access denied.")

#ATm simulation

while True:
    amount=int(input("enter amount:"))
    if amount==0:
        print("No amount")
        break
    else:
        print("Amount available")

#Print prime numbers from 1 to 50,but stop after finding first 5 primes

count=0
num=1
while num<51:
    if num>1:
        i=2
        while i<num:
            if num%i==0:
                break
            i+=1
        else:
            print(num)
            count+=1
            if count==5:
                break
    num+=1

#Take 10 numbers from user skip negative numbers,stop if user enters -999

count=0
while count<10:
    num=int(input("Enter numbers:"))
    if num==-999:
        print("Program stopped")
        break
    if num<0:
        continue
    print("accepted:",num)
    count+=1

