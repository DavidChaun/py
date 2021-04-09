# import this   # python这门语言的禅道，可以打开注释看看 :P 加上#号就是注释一行代码
print("============ let's get started ============")
# ============ let's get started ============

print("============ finish ============")

"""
Q：
编写一个程序，利用随机函数生成15个80~99之间的随机整数，输出其中的最大值与最小值
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
