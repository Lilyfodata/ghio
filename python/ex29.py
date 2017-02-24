#!/usr/bin/python
# -*- coding: utf-8 -*-

people = 25
cats = 30
dogs = 20

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

dogs += 10

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."

# -----------------------------------------------------------------------------
#                           Study Drills
# -----------------------------------------------------------------------------

# 1. if 条件判断语句，if 后面的表达式为真，执行 if 分支的代码语句，否则，执行 if 分支后面的其他语句
# 2. 缩进表示该语句是 if 选择语句的分支，告诉python这是if分支的代码块，根据条件判断，选择执行
# 3. 不缩进，首先收到python错误提示，if语句后面有冒号 : 却没有对应的代码块
# 4. if True or False
#       pass
# 5. 根据改变的数值大小，可以影响后续 if 条件判断的分支选择
