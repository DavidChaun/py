"""
爱德华老师学堂3：今天的内容是介绍循环操作，以及两个经典的、普普通通的算法题~
    算法类型：简单的数列求和，以及根据增长率计算增长时间~
来到第三天，该说的都差不多说完啦，可以出师咯 ( ´▽｀)
出山
"""
# import this   # python这门语言的禅道，可以打开注释看看 :P 加上#号就是注释一行代码
print("============ let's get started ============")
# ============ let's get started ============

"""
for循环（定义不一定准，但是是这么理解的 (￣▽￣) ）：
按理解有经典for循环和增强for循环
普通for循环就是，指定运行次数，运行到指定次数为止；
增强for循环就是：对数组进行遍历，每次从左到右取出一个元素进行操作。
"""
list1 = [18, 6, 39, 0, 42]
# 普通for循环
for i in range(len(list1)):
    print(list1[i])     # 此处i为数组下标，获取对应下标的值，list[i]对应数组的元素
# 增强for循环
for element in list1:
    print(element)      # 每次操作都会从左到右取出元素，element对应数组的元素

"""
无论是普通、还是增强for循环，都可以使用中断或者跳过的操作
"""
print("========== break & continue & else ==========")
for element in list1:
    if element == 6:    # 当element等于6时，跳过本次操作
        continue
    elif element == 0:  # 当element等于0时，中断循环
        break
    print(element)      # 打印了18，39
else:   # 循环结束后，执行的操作。当循环被break时，不会执行else
    pass    # 空语句，避免语法错误的时候可以用 =。=

"""
while循环（for循环的另一种写法，用的比较少，看看就行，昂 ╮(￣▽￣"")╭ ）：
当使用有限的循环操作时，while循环还要在方法体内编写循环中断的条件，因此不如for循环灵活；
但是使用死循环（即不断进行循环内的操作）的时候，就比较方便~因为不用控制循环跳出的条件
死循环示例：不断打印年年18岁这句话
while True:
    print("年年18岁")
"""
count = 0   # 声明一个count变量
while count < 5:    # 当count变量小于5时走while下面的代码，大于等于5时结束循环
    count += 1      # 每次循环的时候count变量+1，给循环一个终结条件
    if count == 2:  # 当count等于2的时候
        continue    # 跳过本次循环
    print("cycling, count = %s" % str(count))     # 当count不等于2时，打印这句话
    if count == 6:  # 当count等于6时
        break       # 中断本次循环，不再执行
else:  # 循环结束后，执行else，当循环被break时，不会执行else
    print("cycle ending. count = " + str(count))


print("============ finish ============")

"""
每日答疑时间 =。=
因为内容比较少，所以今天会有两道题
"""

"""
编写程序，计算 1+2+3+4+...+100
"""
def sum_up(num):
    sum = 0
    content = ""
    for i in range(1, num):
        sum += i
        content += "%d + " % i
    else:
        content = "%s = %s" % (content[0:len(content) - 2], str(sum))  # 使用占位符，参考day2的30行 0.0
        print("和为：%s" % str(sum))
        print("列表公式：%s" % content)


sum_up(101)


"""
假设我国现有人口为12亿，设年增长率为1%，计算多少年后增加到16亿
"""
def calc_increase_years(begin_num, end_num, ratio):
    show_num = begin_num
    years = 0
    while True:
        years += 1
        begin_num += begin_num * ratio
        if begin_num >= end_num:
            print("我国现有人口为%s亿，设年增长率为%s，%d年后增加到%s亿" % (show_num, ratio, years, end_num))
            break


calc_increase_years(12, 16, 0.01)
