#!/usr/bin/python
# -*- coding : utf-8 -*-

#
def print_two (*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)


#
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#
def print_one(arg1):
    print "arg1: %r" % arg1


#
def print_none():
    print "I got nothing."

print_two("ok", "google")
print_two_again("ok", "Google")
print_one("Google")
print_none()
# -----------------------------------------------------------------------------
#                           Study Drills
# -----------------------------------------------------------------------------
# 函数的定义和调用，一个参数，多个参数，以及不含参数
