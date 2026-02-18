# Set

# mutable
# its works based on value
# its allow only unique value
# unordered
# varName = {values}

s  = {10,20,80,90,30,40,50,60,10,50}
print(s)
print(type(s))

# length
print(len(s))

# get particular value
l = [1,2,3,4]
print(l[2])

s  = {1,2,3}
# print(s[2]) type error

# add the value

s = {10,80,30,40,60,20}
s.add(70)
print(s)
s.add(10)
print(s)
# s.add(90,50)  type error
s.add("python")
print(s)

# add multiple value

s = {10,80,30,40,60,20}
g  = {100,200,300}
print(s)
print(g)
s.update(g)
print(s)
print(g)

# list
s = {10,80,30,40,60,20}
l = [100,200,300]
s.update(l)
print(s)

# tuple
s = {10,80,30,40,60,20}
t = (100,200,300)
s.update(t)
print(s)

# int
s = {10,80,30,40,60,20}
i = 55
# s.update(i)

# float

f= 10.23
# s.update(f)

# String
str = "Python"
s.update(str)
print(s)

# remove

s = {10,80,30,40,60,20}
s.remove(10)
# s.remove(100) key error
print(s)

# discard
s = {10,80,30,40,60,20}
s.discard(10)
print(s)
s.discard(100)
print(s)

# pop(index)- cant
# pop()
s = {10,80,30,40,60,20}
# s.pop()
p = s.pop()
print(s)
print(p)

# clear
s = {10,80,30,40,60,20}
print(s)
s.clear()
print(s)

# sort

s = {10,80,30,40,60,20}
st = sorted(s)
print(s)
print(st)
print(type(st))

# copy
s = {10,80,30,40,60,20}
cp = s.copy()
print(s)
print(cp)

# compare
print(s==cp)

# contains - check value present or not
s = {10,80,30,40,60,20}
print(s.__contains__(10))
print(s.__contains__(100))

# in
print(10 in s)
print(100 in s)

# not in
print(10 not in s)
print(100 not in s)

s = {10,80,30,40,60,20}
# max
print(max(s))

# min
print(min((s)))

s  = {"one", "two", "four", "six", "nine"}
print(max(s))
print(min(s))

# union

s1 = {10,20,30,40,50,60}
s2 = {10,50,70,80,90,100,120,30}

print(s1.union(s2))

# intersection - common value

s1 = {10,20,30,40,50,60}
s2 = {10,50,70,80,90,100,120,30}

print(s1.intersection(s2))
print(s1&s2)

# difference

s1 = {10,20,30,40,50,60}
s2 = {10,50,70,80,90,100,120,30}

print(s1.difference(s2))
print(s1-s2)
print(s2.difference(s1))
print(s2-s1)

# symmetric difference

s1 = {10,20,30,40,50,60}
s2 = {10,50,70,80,90,100,120,30}
print(s1.symmetric_difference(s2))
print(s1^s2)

# get all values
# normal loop

s = {10,20,30,40,50,60}
for i in range(0,len(s),1):
     print(s[i])

# Enhanced for loop

for i in s:
    print(i)
    
#Enumerate for loop

print("---------Enumerate---------------")
for i in enumerate(s):
    print(i)

print("---------Enumerate---------------")
for i,v in enumerate(s):
    # print(i)
    # print(v)
    print(i,"-",v)