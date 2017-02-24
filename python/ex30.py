#!/usr/bin/python
# -*- coding: utf-8 -*-

people = 30
cars = 10
trucks = 25

if cars > people: # 比较cars和people的数量，根据数量多少，输出不同的语句
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if not((trucks > cars) and (people > trucks)): # 比较cars和trucks的数量，根据数量多少，输出不同的语句
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks: # 比较people和trucks的数量，根据数量多少，输出不同的语句
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."




# -----------------------------------------------------------------------------
#                           Study Drills
# -----------------------------------------------------------------------------
# 1. elif 是在 if 分支判断为假的时候，进入elif，判断后面的bool表达式真假，为真，则执行elif分值代码块；为假，则继续向下，进入else分支，此时，由于上面判断均为假，直接执行else分值代码块
# 2. 改变数值，影响后面if条件判断的分支，可输出不同内容
# 3. if not((trucks > cars) and (people > trucks)):
