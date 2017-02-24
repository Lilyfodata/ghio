#!/usr/bin/python
# -*- coding : utf-8 -*-
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

# -----------------------------------------------------------------------------
#                           Study Drills
# -----------------------------------------------------------------------------
# raw_input() 读取用户输入到终端的内容，与用户交互，任何类型的输入都可以接受，默认返回字符串类型
# raw_input('> ') 带有提示性标识，提醒用户输入。 int(raw_input()) 将用户输入的内容转成数字
# 受 %r 的影响，输出显示 '6\'2"'，因为已经有了 " ，所以整体用 ' ，字符串本身带的 ' ，需要用转义字符 \ 
