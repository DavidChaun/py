"""
爱德华老师学堂15：
2021.01.15
学堂最近拖更了 (。>︿<)
主要还是受到了公司压迫 计划多 给的时间少

（忽然想到了一句歌词：大家忙，多么漂亮理由... 沟通少了很多）

最近舍友回老家发展了，说不能这么颓废
少了个人在宿舍，确实很空荡，习惯了回到宿舍的时候灯亮有热水喝的日子 ╮(╯-╰)╭
但确实更加自由了，也没人打扰 =。= 想做什么也方便一点
想起之前给你写信的时候，我只能趁他睡觉的时候偷偷写 哈哈哈（所以字写的丑多多少少有他的影响）

虽然你很忙，但是我也没闲下来，我也有目标的 (ง •_•)ง
最近在复习点考题，准备些面试的资料，争取年后离开这个窝
（毕竟没多少挑战性）

努力争取一下，看能不能进YY 哈哈哈

"""
# import this   # python这门语言的禅道，可以打开注释看看 :P 加上#号就是注释一行代码
print("============ let's get started ============")
# ============ let's get started ============

print("============ finish ============")

"""
每日答疑时间 =。=
因为没有基础语法教了，只能讲解题目了hhh
"""

"""
Q：
编写一段代码，求给定的一个圆的周长和面积。要求：
（1）圆的半径r利用input函数从键盘任意输入（r>0)
（2）圆周率定义为符号常量
（3）利用赋值语句将求出的周长和面积赋值给变量L和s
（4）用print方法输出详细结果

A：
好家伙，直接是一整道题目

"""
def circle():
    r = input("请输入圆的半径r：")
    pi = "Π"
    print("圆的周长为：L = %s" % (str(int(r)*2) + pi))
    print("圆的面积为：s = %s" % (str(int(r)**2) + pi))

circle()

print("============ 中场休息的分割线 ============")

"""
Q：
计算数学表达式 1 - 2/2! + 3/3! - 4/4! + ... + (-1)^(n+1)*n/n! 的程序

A：
这题目，跟我当时亲自指导的题目好像啊 hhh

"""
def sum_step_multiply(num):
    sum_up = 0
    for i in range(1, num + 1):
        step_temp = 1
        for j in range(1, i+1):
            step_temp *= j
        sum_up += (-1)**(i+1)*i/step_temp
    return sum_up
