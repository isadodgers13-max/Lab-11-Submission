# lab11.py
# CS 3035 - Lab 11: Data Types & Static-Dynamic-Duck Typing

# ---------------------------
# Part 1: Data Types & Conversions
# ---------------------------

print("=== Part 1: Data Types & Conversions ===")
print("int:", 42, type(42))
print("float:", 3.14, type(3.14))
print("bool:", True, type(True))
print("str:", "hello", type("hello"))
print("list:", [1, 2, 3], type([1, 2, 3]))
print("tuple:", (1, 2), type((1, 2)))
print("dict:", {"a": 1, "b": 2}, type({"a": 1, "b": 2}))
print("set:", {1, 2, 3}, type({1, 2, 3}))
print("NoneType:", None, type(None))

# Conversions
print("\nConversions:")
print("int('123') =", int("123"))
print("float('1.5') =", float("1.5"))
print("str(10) =", str(10))
print("list('abc') =", list("abc"))
print("set([1,1,2]) =", set([1, 1, 2]))


# ---------------------------
# Part 2: Static vs Dynamic Typing
# ---------------------------

print("\n=== Part 2: Static vs Dynamic Typing ===")

# Dynamic rebinding
x = 10
print("x =", x, type(x))
x = "hello"
print("x =", x, type(x))

# Functions
def add(a, b):
    return a + b

def add_ints(a: int, b: int) -> int:
    return a + b

# Calls
print("add(3, 4) =", add(3, 4))
print("add('Hi', 'There') =", add("Hi", "There"))

try:
    print("add_ints(3, '4') =", add_ints(3, "4"))
except TypeError as e:
    print("Caught TypeError:", e)


# ---------------------------
# Part 3: Duck Typing
# ---------------------------

print("\n=== Part 3: Duck Typing ===")

def parade(thing):
    try:
        print(thing.quack())
        print(thing.walk())
    except AttributeError:
        print("Not duck-like.")

class Duck:
    def quack(self): return "quack!"
    def walk(self):  return "waddle"

class Rock:
    pass

# Demonstration
parade(Duck())
parade(Rock())
