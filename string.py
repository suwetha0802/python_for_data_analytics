s = "welcome"

print(s)
print(type(s))

# lenght

print(len(s))
l=len(s)
print(l)

# get particular value

# slice operator

s = "welcome"
print(s[3])
print(s[-3])

# varName[start:stop:in/dr]

print(s[1:5:1])
print(s[1:5:2])
print(s[1:5:])
print(s[1:])
print(s[:5])
print(s[:])
print(s[-2:-5:-1])
print(s[-5:-2])
# print(s[7])  index error

# index value

s = "welcome to python"

print(s.index('m'))
# print(s.index('q')) value error
print(s.index("to"))
print(s.index(" "))
print(s.index('e'))
print(s.rindex('e'))

# find

print(s.find("m"))
print(s.find('q'))
print(s.find('to'))
print(s.find(' '))
print(s.find('e'))
print(s.rfind('e'))

print("-----starting------")

s = "Welcome to python"

print(s.startswith("Welcome"))
print(s.startswith("welcome"))
print(s.startswith("Wel"))
print(s.startswith("W"))
print(s.startswith("to"))
print(s.startswith("python"))
print(s.startswith(" "))

print("------------Ending----------")

print(s.endswith("Welcome"))
print(s.endswith("python"))
print(s.endswith("on"))
print(s.endswith("n"))

# check the letter or word present or not

s = "Welcome to python"
print(s.__contains__("on"))
print(s.__contains__(" "))
print(s.__contains__("loc"))
print(s.__contains__("lo"))
print(s.__contains__("th"))
print(s.__contains__("python"))

# in

print("Welcome" in s)
print("Wel" in s)
print(" " in s)
print("java" in s)
print("me" in s)

# replace

s = "hello"
re = s.replace('l' , "#")
print(s)
print(re)
print(s.replace('h', 'H'))

s = "welcome to python"
# print(s.replace('to', 2))
print(s.replace('to','2'))

# compare a string

s = "hello"
c = "Hello"

print(s==c)

# join the strings

print(s+c)

s = "wELCOME"
# upper

up = s.upper()
print(s.upper())
print(s.isupper())
print(up.isupper())

# lower

lo = s.lower()
print(s.lower())
print(s.islower())
print(lo.islower())

print(s.capitalize())

# title

s = "welcome to python"
print(s.title())

# remove unwanted space

s = "   welcome to python   "
print(s)

print(s.strip())
print(s.lstrip())
print(s.rstrip())

# for loop

s = "python"

for i in range(0,len(s),1):
    print(s[i])

# enhanced for loop

for i in s:
    print(i)