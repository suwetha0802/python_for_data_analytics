#Dictionary

# variableName = {keys:values}

d = {10:"Java", 20:"Python", 30: "C++", 40: "Selenium", 50 : "Dart", 60 : "Flutter"}
print(d)

print(type(d))

# Length
print(len(d))


# get particular value

d = {10:"Java", 20:"Python", 30: "C++", 40: "Selenium", 50 : "Dart", 60 : "Flutter"}
print(d[20])
v = d[20]
print(v)
# print(d[70])  Key error

# get()

print(d.get(30))
v = d.get(30)
print(v)

# add values

d = {10:"Java", 20:"Python", 30: "C++", 40: "Selenium", 50 : "Dart", 60 : "Flutter"}
print(d)
# storeVarName[new key] = new Value
d[70] = "Sql"
print(d)

# add multiple value

d = {10:"Java", 20:"Python", 30: "C++", 40: "Selenium", 50 : "Dart", 60 : "Flutter"}
g = {100 : "Mon", 200 : "Wed"}
print(d)
d.update(g)
print(g)
print(d)

# Replace
# storeVarName [existingkey] = value

print(d)
d[50]= "Ruby"
print(d)

# remove

d = {10:"Java", 20:"Python", 30: "C++", 40: "Selenium", 50 : "Dart", 60 : "Flutter"}
# pop(key)
p = d.pop(20)
print(d)
print(p)

# popItem()

d = {10:"Java", 20:"Python", 30: "C++", 40: "Selenium", 50 : "Dart", 60 : "Flutter"}
pi = d.popitem()
print(d)
print(pi)

# clear

d = {10:"Java", 20:"Python", 30: "C++", 40: "Selenium", 50 : "Dart", 60 : "Flutter"}
print(d)
d.clear()
print(d)

# Copy

d = {10:"Java", 20:"Python", 30: "C++", 40: "Selenium", 50 : "Dart", 60 : "Flutter"}
cp = d.copy()
print(d)
print(cp)

# max

d = {10:"Java", 20:"Python", 30: "C++", 40: "Selenium", 50 : "Dart", 60 : "Flutter"}
print(max(d))

# min

d = {10:"Java", 20:"Python", 30: "C++", 40: "Selenium", 50 : "Dart", 60 : "Flutter"}
print(min(d))

# compare
print(d==cp)

# get only keys

d = {10:"Java", 20:"Python", 30: "C++", 40: "Selenium", 50 : "Dart", 60 : "Flutter"}
k = d.keys()
print(k)
print(type(k))

# get only values

d = {10:"Java", 20:"Python", 30: "C++", 40: "Selenium", 50 : "Dart", 60 : "Flutter"}
v = d.values()
print(v)
print(type(v))

# get keys and values as a pair

d = {10:"Java", 20:"Python", 30: "C++", 40: "Selenium", 50 : "Dart", 60 : "Flutter"}
it = d.items()
print(it)
print(type(it))
print(d)

# get all value

d = {10:"Java", 20:"Python", 30: "C++", 40: "Selenium", 50 : "Dart", 60 : "Flutter"}

print("Enhanced for loop")

for i in d.items():
    print(i)

for k,v in d.items():
    # print(k)
    # print(v)
    print(k,"=",v)

print("Enumerate for loop")
for i in enumerate(d.items()):
    print(i)

for i, v in enumerate(d.items()):
    # print(i)
    # print(v)
    print(i,"-",v)

# convert anything to list

l = [1,2,3]
t = (1,2,3)
s = {1,2,3}
print(list(l))
print(list(t))
print(list(s))
a = list(l)
b = list(t)
c= list(s)
print(type(a))
print(type(b))
print(type(c))

# Anything convert to tuple

l = [1,2,3]
t = (1,2,3)
s = {1,2,3}
print(tuple(l))
print(tuple(t))
print(tuple(s))
a = tuple(l)
b = tuple(t)
c = tuple(s)
print(type(a))
print(type(b))
print(type(c))

# Anything convert to set

l = [1,2,3]
t = (1,2,3)
s = {1,2,3}
print(set(l))
print(set(t))
print(set(s))
a = set(l)
b = set(t)
c = set(s)
print(type(a))
print(type(b))
print(type(c))