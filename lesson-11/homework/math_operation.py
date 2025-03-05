from math import pi
# 1. Create your own virtual environment and install some python packages.
# 2. Create custom modules
# math_operations.py
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    if b!=0:
        return a/b
    else:
        return 'Cannot divide by zero'
        
