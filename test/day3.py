# import this   # python这门语言的禅道，可以打开注释看看 :P 加上#号就是注释一行代码
print("============ let's get started ============")
# ============ let's get started ============

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
