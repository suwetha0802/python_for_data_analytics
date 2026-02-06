# =========================================
# Python Type Conversion Practice
# Author: Suwetha
# Description: Basic type conversion examples
# =========================================

print("----- Integer Conversion -----")
print(int(10))
print(int(10.23))
print(int(True))
print(int(False))
print(int(True + True))
print(int("10"))

# The following lines cause errors (for learning purposes)
# print(int("10.23"))   # ValueError
# print(int("one"))     # ValueError
# print(int(10+3j))     # TypeError
# print(int(True/False)) # ZeroDivisionError


print("\n----- Float Conversion -----")
print(float(10))
print(float(10.23))
print(float(-10.23))
print(float(True))
print(float(False))
print(float("10"))
print(float("10.23"))

# Error examples
# print(float("True"))   # ValueError
# print(float(10+4j))    # TypeError


print("\n----- Complex Conversion -----")
print(complex(10))
print(complex(10.23))
print(complex(10 + 4j))
print(complex(True))
print(complex(False))
print(complex("10"))
print(complex("10+2j"))
print(complex(10, 10))
print(complex(10.1, 10.3))

# Error examples
# print(complex("10","10"))   # TypeError
# print(complex(True/False))  # ZeroDivisionError


print("\n----- Boolean Conversion -----")
print(bool(10))
print(bool(1))
print(bool(0))
print(bool(10.23))
print(bool(10 + 5j))
print(bool("10"))
print(bool(""))
print(bool(" "))
print(bool("welcome to python"))
print(bool("0"))


print("\n----- String Conversion -----")
print(str(10))
print(str(10.3))
print(str(True))
print(str(False))
print(str(10 + 3j))
print(str(True + False))
print(str(True + True))
print(str("10"))
print(str("10.3"))
print(str("false"))
print(str("True+True"))
print(str("one"))

# Error examples
# print(str(one))   # NameError
# print(str(true))  # NameError