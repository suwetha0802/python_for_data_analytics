#List

# Ordered - items keep their position
# duplicate
# multiple value and multiple datatype we can store
# mutable

# varName = [values]

#     0  1   2     3     4   5    6
l = [10,50,53.23,"Sai",True,5+5j,10]
#     -7 -6  -5    -4   -3   -2   -1

print(l)
print(type(l))

# Length
print(len(l))

# get a particular value

# Slice operator

print(l[4])
print(l[2])
print(l[-2])
# print(l[7]) Index Error

print(l[1:5:1])
print(l[1:5:2])
print(l[1:5:])
print(l[1:])
print(l[:5])
print(l[:])
print(l[-5:-2])
print(l[-2:-5:-1])

# index

#    0  1  2  3  4  5  6  7  8  9 10 11  12
l= [10,20,30,80,90,40,50,10,60,70,60,10,50]

print(l.index(10))
print(l.index(10,1))
print(l.index(10,8))
print(l.index(10,1,8))
# print(l.index(100)) value error

# Add values in list

l= [10,20,80,60,30]
print(l)
# append

l.append(100)
print(l)
l.append(200)
print(l)

# l.append(300,400) Type error

l.append([1,2,3])
print(l)
print(l[7])
print(l[7][1])

# insert

l.insert(2,40)
print(l)

l.insert(3,[7,8,9])
print(l)
print(l[3])
print(l[3][2])

# add multiple value
# l.extend(10) Type error
l.append("Hello")
print(l)
l.extend("Hello")
print(l)

# l.extend(9,8,7) Type error

l.extend([9,10,11])
print(l)

# Remove a values in list

l = [10,80,90,40,60,20,70,30]
print(l)
# remove

l.remove(40)
print(l)
# l.remove(100) value error

# pop

l.pop()
print(l)

# pop(index)

l.pop(1)
print(l)

# del

del l[2:4]
print(l)

# clear

l.clear()
print(l)

# Replace

l = [10,80,90,60,20,70, 30]
print(l)

l[2] = 200
print(l)
# l[8] = 100  Index error

# Reverse

l = [10,80,90,60,20,70,30]
print(l)
l.reverse()
print(l)

# sort

l = [10,80,90,60,20,70, 30]
print(l)
l.sort()
print(l)

l.sort(reverse= True)
print(l)

# sorted

l = [10,80,90,60,20,70, 30]
print(l)
st = sorted(l)
print(st)

l = [10,80,90,60,20,70, 30]

# Max
print(max(l))
# min
print(min(l))

# Copy

l = [10,80,90,60,20,70, 30]
cp = l.copy()
print(l)
print(cp)

# Compare
print(l==cp)

l = [1,2,3,6,4,9,7,7,2,9,4,1,1,1]
# count

print(l.count(1))
print(l.count(4))
print(l.count(7))

l = [10,20,30,60,40,80,90]

# Normal for loop

for i in range(0,len(l),1):
    print(l[i])

#Enhanced for loop

for i in l:
    print(i)

#Enumerate for loop
for i in enumerate(l):
    print(i)

for i,v in enumerate(l):
    # print(i)
    # print(v)
    print(i,"-",v)
# 0 - 10