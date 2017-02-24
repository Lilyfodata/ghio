#!/usr/bin/python
# -*- coding : utf-8 -*-

from sys import argv
script, first, second, third, anthoer = argv

print "The script is called:", script
print "The first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# -----------------------------------------------------------------------------
#                           Study Drills
# -----------------------------------------------------------------------------
# valueError: need more than 1 value to unpack
#
from sys import argv
script, first, second = argv

print "你好，我叫：", script
print "你给我的第一个词是：", first
print "还有第二个：", second

print "没玩够？在写一个..."
third = raw_input('> ')
print "可以了，最后一个是：", third
