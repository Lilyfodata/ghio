#!/usr/bin/python
# -*- coding: utf-8 -*-
cars = 100 # 车的数量
space_in_a_car = 4.0 # 每辆车可使用的空间
drivers = 30 # 驾驶员数量
passengers = 90 # 乘客数量
cars_not_driven = cars - drivers # 没有被驾驶的车辆数量
cars_driven = drivers # 被驾驶的车辆数量 = 驾驶员数量
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

print "Hey %s there." % "you"

# -----------------------------------------------------------------------------
#                           Study Drills
# -----------------------------------------------------------------------------
# 牵扯到数学计算的题目中，应该注意多使用浮点数，可以更加接近实际情况，不然python默认四舍五入以后，会丢失计算的精度。
