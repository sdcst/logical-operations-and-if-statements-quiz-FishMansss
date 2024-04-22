#!python3
"""
Debug this program so that it runs

original code:
x = input("enter a decimal number"))
xi = int(x)
if (x - xi) == 0:
    print(f"{x} is an integer")
"""
import math
x = input("enter a decimal number")
x = float(x)
xi = int(x)
if (x - xi) == 0:
    x = int(x)
    print(f"{x} is an integer")
    