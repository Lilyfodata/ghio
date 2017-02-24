#!/usr/bin/python
# -*- coding: utf-8 -*-
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_cm = 2.54 * height
weight = 180 # lbs
weight_kg = weight * 0.45
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)

print "my %r you"
print "%r"
print round(1.07333)#四舍五入
