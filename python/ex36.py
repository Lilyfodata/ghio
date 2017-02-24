#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 修改自ex35.py，修改部分逻辑，增加一个选择
from sys import exit

def kiss_or_not():
    kiss = raw_input("> ")

    if kiss == "亲":
        print "趁人家睡着偷偷亲别人，你还是人吗？"
    elif "不亲" in kiss:
        print "你这么见死不救，禽兽不如！"
    else:
        print "你干嘛呢，只是问你亲不亲。"
    kiss_or_not()


def gold_room():
    print "骚年，这里充满了黄金。所以你想做点什么吗，说吧，想要多少？"

    choice = raw_input("> ")
    if choice.isdigit():
#    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("别太贪心，给我一个可以读取的数量！")

    if how_much < 5000000:
        print "看不起我，才要这么点！"
        exit(0)
    elif how_much > 10000000:
        dead("想死吗？要这么多...")
    else:
        print "你拿到的金币受到了诅咒！女孩瞬间变成了睡美人！"
        print "想救醒她，需要亲吻她；可是救醒她以后，她就会忘记你。"
        print "亲，还是不亲？"
        kiss_or_not()



def girl_room():
    print "屋子里有4个女孩；"
    print "每个女孩都戴着口罩；"
    print "解下女孩的口罩，你将得到她的爱；"
    print "所以你喜欢什么样的女孩？（胖的 瘦的 身材高 身材矮）"
    say_yes = False

    while True:
        choice = raw_input("> ")

        if choice == "胖的":
            dead("女孩太激动没站稳，摔倒把你压死了！")
        elif choice == "瘦的" and not say_yes:
            print "你看见她太瘦了，想给她买吃的，可是你没有钱。女孩看起来有些生气"
            say_yes = True
            print "可是她说了yes，试着温柔点叫她"
        elif choice == "瘦的" and say_yes:
            print "旁边有扇门，你想拽着她私奔..."
            gold_room()
        elif choice == "身材高":
            dead("别做梦了，她身高上百米，你根本够不着摘口罩！")
        elif choice == "身材矮":
            dead("住手，人家还是未成年！")
        else:
            print "注意：只有四个女孩！"

def ghost_room():
    print "这里是你的梦境！"
    print "你的梦境被别人盗窃了，你如何走出去？"
    print "是选择自虐，痛醒；还是选择在梦境里面编程？"

    choice = raw_input("> ")

    if "自虐" in choice:
        print "咦，想不到你喜欢这个口味。那就再来一次..."
        start()
    elif "编程" in choice:
        dead("你已触动梦境自毁程序，3.2.1... game over!")
    else:
        ghost_room()

def dead(why):
    print why, "死心了吗！"
    exit(0)

def start():
    print "游戏开始，你有两个选择！"
    print "吞下蓝药丸 还是红药丸"

    choice = raw_input("> ")

    if "红" in choice:
        girl_room()
    elif "蓝" in choice:
        ghost_room()
    else:
        dead("你又忘记吃药了，")

start()
