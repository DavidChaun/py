"""
爱德华老师学堂14：
2021.01.08 - 2021.01.10
本来8号想发的，因为这周陪你相当开心，所以拖到了10号(。・∀・)ノ

今天看到你的眼影，很漂亮呀 ~ ~ 我一直看你竟忘了开口
还有收到了你的礼物，真是超级开心的 (*^▽^*)
而且是面膜，真是好特别的礼物，我第一次收到面膜，好开心

因为脸上痘痘的原因，啥都要忌口
怪我这段日子，不能吃牛羊煎炸的食物，所以你选择范围小了很多，遗憾了啊
天气冷我也很想和你一起吃火锅的，我会尽快恢复的啦 ~ ~

其实星期六想一起去正佳海洋馆的，但是你的导师有点坏我好事喔
然后我看了下日期，17号你要去珠海，感觉下周就没什么机会见面了
然后25号你就要放假了，我估计要等到20多号可能才能见到你了，期待中

我朋友说我认识了你之后，整个人积极向上了
弗洛伊德曾经说过，这就是灯塔的力量吧

快乐的时光总是过得很快，期待下一次的见面

我也要努力啦，一起努力
Fight for a better tomorrow ！！ ~~
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
编写一个程序，利用随机函数生成15个80~99之间的随机整数，输出其中的最大值与最小值

A：
随机数生成数字然后放入数组=。=15个数的最大与最小值，一下就能想到冒泡算法了吧？然后取数组头尾即可 ~ ~ 其实数列默认方法也有排序的
"""
import random

def random_num_sort():
    num_list = []
    while len(num_list) < 15:   # 当数组里面不够15个的时候，不要跳出循环
        num_list.append(random.randint(80, 99))     # 往数组里面塞随机数

    print("随机数数组，排序前：" + str(num_list))
    # 冒泡算法复习，刻在DNA里面的操作
    for i in range(15):
        for j in range(i + 1, 15):
            if num_list[i] > num_list[j]:
                num_list[i], num_list[j] = num_list[j], num_list[i]

    # 实在忘记冒泡可以使用内置函数
    # num_list.sort()

    print("随机数数组，排序后：" + str(num_list))
    print("80~99之间的随机整数，其中的最大值 max=%d" % num_list[len(num_list) - 1])
    print("80~99之间的随机整数，其中的最小值 min=%d" % num_list[0])

    return num_list[len(num_list) - 1], num_list[0]


random_num_sort()

print("============ 中场休息的分割线 ============")

"""
Q：
单击窗体产生10个2位的随机正整数，计算并显示出最大的数据和其在数组中的位置

A：
单击窗口就大可不必了=。= 把10个2位的随机正整数都放入数组，然后可以用内置函数解决 =。= 
但是用内置函数有点低端，所以我还是写一下手算的

"""
def random_num_list_find_one():
    num_list = []
    while len(num_list) < 10:       # 当数组里面不够15个的时候，不要跳出循环
        num_list.append(random.randint(10, 99))     # 往数组里面塞随机数

    print("随机数数组，排序前：" + str(num_list))

    # 查找最大的数字以及索引
    max_num = num_list[0]
    max_num_index = 0

    for i in range(10):
        if num_list[i] > max_num:
            max_num = num_list[i]   # 当数组内的数字大于之前的赋值时，直接替换
            max_num_index = i

    # 下面是内置函数
    # max_num = max(num_list)
    # max_num_index = num_list.index(max_num)

    print("随机数数组，排序后：" + str(num_list))
    print("10个2位的随机正整数，其中的最大值 max=%d" % max_num)
    print("10个2位的随机正整数，其中的最大值的索引 index=%d" % max_num_index)
    print("10个2位的随机正整数，其中的最大值的位置为： %d" % (max_num_index + 1))


random_num_list_find_one()
