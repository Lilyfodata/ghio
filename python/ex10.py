#!/usr/bin/python
# -*- coding : utf-8 -*-
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
    for i in ["/","-","\\","|","/","-","\\","|"]:
        print "%s\r" % i,

# -----------------------------------------------------------------------------
#                           Study Drills
# -----------------------------------------------------------------------------
# %r 输出含有对象属性的内容，调试的时候可用，%s 更多用来显示输出到终端。