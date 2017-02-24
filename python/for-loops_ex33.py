#!/usr/bin/python
# -*- coding: UTF-8 -*-


def terms_append(terms_v, step = 1):
    n = 0
    terms = []

    if step <= 0:
        step = 1

    for i in range(n, terms_v, step):
        print "for开始的时候 i = %d" % i
        terms.append(i)
        print "terms里面的值: ", terms
        print "for结束的时候 i = %d" % i

    print "for结束以后，terms的值: "

    for term in terms:
        print term,


print "\n\t想不想创建一个从0开始的list？(Y/N)"
yorn = raw_input("> ")

if yorn == "Y" or yorn == "y":
    print "你想要一个多长的list？给我一个数："
    list_len = int(raw_input("> "))
    print "你还可以选择给我一个表示步长的数，默认是1，输入<=0的数不设置："
    step_len = int(raw_input("> "))
    terms_append(list_len, step_len)

elif yorn == "N" or yorn == "n":
    print "你确定你没选错？"

else :
    print "看清楚是Y和N,,"
