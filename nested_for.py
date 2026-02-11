#Nested for

#Example 1

for i in range(0,4,1):
    for j in range(0,3,1):
        print(j,end=" ")
    print(i)

#Exampe 2

for i in range(4):
    for j in range(4):
        print("*",end=" ")
    print(i)

#Exampe 3

for i in range(1,5):
     for j in range(i):
         print(j,end=" ")
     print()

#Example 4

for i in range(1,6):
    for j in range(5-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()


