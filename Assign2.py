"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
import math
hpresent = 0
print("Enter a number:")
x = input()
x = float(x)
print("Enter another number:")
y = input()
y = float(y)
print("is one of the numbers the hypotenuse of a right triangle?")
print("        'y' for yes 'n' for no")
hpresent = input()
if hpresent == "y":
    if x>y:
        bignum = x
        smallnum = y
    if y>x:
        bignum = y
        smallnum = x
    ##missing side is z
    z = (bignum**2 - smallnum**2)**0.5
    print(z)
    input()
if hpresent == "n":
    hyp = (x**2 + y**2)**0.5
    round(hyp,1)
    print(hyp)
    input()
else:
    exit()