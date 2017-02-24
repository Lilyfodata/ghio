#!/usr/bin/python
# -*- coding : utf-8 -*-
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

# -----------------------------------------------------------------------------
#                           Study Drills
# -----------------------------------------------------------------------------
# But it didn't sing. 这一句里面有了一个 ' ，所以输出的时候用 "" 引起来。
