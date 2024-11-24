def add(a,b):
        return a+b 

def subtract(a,b):
        return a-b

def multiply(a,b):
        return a*b

def divide(a,b):
        return a/b

def power(a,b):
        return a**b

def square_root(a):
        return a**0.5

def square_root(b):
        return b**0.5

print("this is the simple calculator for the basic arthmativ operations.")

print("Available operations are: divide and multiply and subtract, and power, and square root,addition.")

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

print("Addition:", add(a,b))

print("Subtraction:", subtract(a,b))

print("Multiplication:", multiply(a,b))

print("Division:", divide(a,b))

print("Power:", power(a,b))

print("Square Root:", square_root(a))

print("Square Root:", square_root(b))