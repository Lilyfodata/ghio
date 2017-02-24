#!/usr/bin/python
# -*- coding : utf-8 -*-

def add(num1, num2):
    print "ADDING %d + %d" % (num1, num2)
    return num1 + num2

def subtract(num1, num2):
    print "SUBTRACTING %d - %d" % (num1, num2)
    return num1 - num2

def multiply(num1, num2):
    print "MULTIPLYING %d * %d" % (num1, num2)
    return num1 * num2

def divide(num1, num2):
    print "DIVIDING %d / %d" % (num1, num2)
    return num1 / num2


print "Let's do some math with just functions!"

age = add(20, 7)
height = subtract(200, 5)
weight = multiply(60, 2)
iq = divide(1000, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"


# -----------------------------------------------------------------------------
#                           Study Drills
# -----------------------------------------------------------------------------



# my own function, return something
def fname():
    return "hello world"

mystr = fname()
print mystr

# the normal formula
divide_v = divide(iq, 2)
multiply_v = multiply(weight, divide_v)
subtract_v = subtract(height, multiply_v)
what_v = add(age, subtract_v)

print "That becomes: ", what_v, "Yes, I can do it by hand!"

# another value.
divide_v2 = divide(iq * 4, 4)
multiply_v2 = multiply(weight, divide_v2)
subtract_v2 = subtract(height, multiply_v2)
what_v2 = add(age, subtract_v2)

print "That becomes: ", what_v2, "Yes, I can do it by hand!"

# simple formula
simple = divide(multiply(iq, add(weight, subtract(height, age))), 2)

print "That becomes: ", simple, "Can you do it by hand?"
