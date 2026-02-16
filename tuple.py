#TUPLE

# tuple is ordered
# index
# multiple values and multiple datatypes we can store
# faster than list

#Syntax

# varName = (values)

t = (10,20,30,40,50,70,80,60,90)

print(t)
print(type(t))

# length
print(len(t))

# get particular value

# slice operator
t = (10,20,30,40,50,70,80,60,90)

print(t[4])
print(t[-4])
print(t[1:5:1])
print(t[1:5:2])
print(t[1::])
print(t[:5])
print(t[:])
print(t[-5:-2])
print(t[-2:-5:-1])

# index of value

t = (10,20,30,40,10,50,70,80,60,90,10)
print(t.index(40))
# print(t.index(45))  type error
print(t.index(10))
print(t.index(10,7))
print(t.index(10,1,8))

# add values

t = (10,20,30,40,10,60,90,80,10,70,30,60)
g =(100,200,300)

v = t+g
print(v)
print(t)
print(g)

# remove 

t = (1,2,3,4,5,6,7,8,9)

print(t)
print(t[:3])
print(t[4:])
print(t[:3]+t[4:])
print(t)

# replace

l = [1,2,3,4]
l[0] = 5
print(l)

t = (1,2,3)
# t[0] = 4
# print(t) type error

# count

t= (10,50,90,10,30,10,50,60,70,80,50)
print(t.count(10))
print(t.count(100))

# max
t = (10,30,20,50,40,60,70,80,90)
print(max(t))

# min
print(min(t))

t = ("mon","tue","wed","thr","fri")
print(max(t))
print(min(t))

# check a value present or not

t = (10,20,30,90,40,50)
print(t.__contains__(10))
print(t.__contains__(100))

# in
print(10 in t)
print(100 in t)

# not in
print(10 not in t)
print(100 not in t)

# sort
t = (10,20,30,90,40,50)

print(sorted(t))
print(type(sorted(t)))

# get all values

# normal for loop

t = (10,20,30,90,40,50)
for i in range(0,len(t),1):
    print(t[i])

# Enhanced for loop

for i in t:
    print(i)

# enumerate

for i in enumerate(t):
    print(i)

for i, v in enumerate(t):
    # print(i)
    # print(v)
    # print(i,":",v)
    print(v,":",i)