#!/usr/bin/python
# -*- coding: utf-8 -*-
import string
import re
from nltk import bigrams
from collections import Counter
from zhon.hanzi import punctuation
file = open("happiness_seg.txt")

line_all = []
for line in file:
    line = line.strip()

    if line:
        line = re.sub(ur"[%s]+" %punctuation, " ", line.decode("utf-8")) # 使用正则表达式，匹配文章中的标点符号，用空格替换
        line = line.split(' ') # 按照空格，将每一行分割成list
        line_all.extend(line) # 将所有list拼接起来，组成最终list
        #print line
print  line_all

Counter(bigrams(line_all))
# bigrams(line_all) 可以将最终list中的每两个相邻元素两两组合，组成二元词组
# Counter 统计每一个二元词组出现的次数。