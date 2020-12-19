"""
爱德华老师学堂1：今天的内容是基础类型，运算符，以及一个冒泡算法的解释
既然是为了应试而学，那我认为是不需要学得太深入，1~3日我会介绍一下基础语法，往后会重点往算法题解析~方便你使用python这门语言 =。=
因为今天是第一天哦，所以先介绍一下python的类型以及运算符，如果你已知悉，那今天会是相当轻松的一天~~也可以当作温故而知新喔
本文在你已经会打印hello world的前提下编写 :P
Now is better than never.
"""
# import this   # python这门语言的禅道，可以打开注释看看 :P 加上#号就是注释一行代码
print("============ let's get started ============")
# ============ let's get started ============

"""
py3主要的5种基础类型：
int（整型） 
float（浮点型，即小数 or 科学计数） 
sting（字符串） 
布尔型（True，False，注意单词前面要大写）
虚数（复数3+5j（i换成了j），不常用，忽视）
"""
numInt = 12  # 整型
# 多个赋值，可以省略等号？？  在交换两个变量的值时非常高效~
# 等同 a=1（整型），b=3.1415926（浮点型），c="baby"（字符串），d=3 + 5j（虚数），e=True
a, b, c, d, e = 1, 3.1415926, "baby", 3 + 5j, True

"""
拥有了变量，就可以进行运算啦>.<
下面是运算符的介绍和使用，篇幅不小=。=
"""
# + - * / 对应加减乘除，烂熟于心，也没有能玩出花的操作
plusOperate, substractOperate, multiplyOperate, divideOperate = (1 + 1), (1 - 1), (1 * 1), (1 / 1)
# % 取余，除法运算后取余数部分
print(3 % 2)    # 3 / 2 余数为1
# 数值间可以相加，布尔值的话，True等同于数值 1，False等同于数值 0
print(1 + 1.32 + 5j + True + False)     # (3.3200000000000003+5j)
# 注意，字符串不可以和数值直接相加，需要把数值转为字符串
print("1 + 1 = " + str(2))

# ** 幂 - 返回x的y次幂
print(2 ** 3)  # 8
# // 取整除 - 返回商的整数部分（向下取整）
print(-9 // 2)  # -5，原本结果等于-4.5，需要整数往小的取为-5

# 赋值运算符，+=，-=，*=，/=，**=，//=
num1 = 0
num1 += 2   # 等同 num1 = num1 + 1
num1 **= 3  # num1 = (0 + 2) 的三次方
print(num1)

# 比较运算符：比较两个值，得到布尔值，有 >（大于） >=（大于等于） <（小于） <=（小于等于） ==（等于） !=（不等于）
print(2 >= 1)   # True

"""
逻辑运算符：
条件1 and 条件2（且） 
条件1 or 条件2（或者） 
not(条件)（否）
"""
print(1 == 1 and 2 == 2)    # True；条件1与条件2都为True时，输出为True
print(1 == 1 or 1 == 2)    # True；其中一个条件输出为True时，输出为True，否则为False
print(not(1 == 1))  # False；将条件的布尔值反转，条件输出为True时，not(条件)输出为False

"""
成员运算符：
in : 如果在指定的序列中找到值返回 True，否则返回 False。
not in : 
"""
tuple1 = (3, 4, 1)
print(3 in tuple1)  # True
print(233 in tuple1)  # False

"""
身份运算符（估计用不上，可以忽略）：
is : 类似==，对象比较时会比较内存地址，==在对象比较时是比较值
is not : 类似!=
"""
print(str(1) is str(1))     # False 两个新建的字符串对象，内存地址不一样
print(str(1) == str(1))     # True 虽然内存地址不一样，但是值是一样的，都是 "1"

print("============ finish ============")

"""
每日答疑时间 =。=
"""
# 冒泡算法
def bubble_sort(list):
    n = len(list)   # 内置函数len()，获取序列或者字符串的长度
    for i in range(n):  # 循环1：该操作是遍历。假设n为3，i从0开始，每次完成一次操作i加1，当i=3时（不包括i=3时的操作），退出此次循环
        for j in range(i + 1, n):   # 循环2：遍历操作，range(num1, num2)意思是，从num1开始，到num2结束（不包括num2的操作）；range(num)等同与range(0, num2)
            if list[i] > list[j]:   # 下标i的元素与下标j的元素交换，大的值往后
                list[i], list[j] = list[j], list[i]     # list[i] 假设i=1时，取数组下标为1的元素（即序列从左数的第二个元素）
    else:   # 循环1结束时，执行else部分的语句
        print(list)
        print("数组长度为：%d" % len(list))   # %d 是字符串占位符，配合 % 运算符，使用len(list) 取代%d部分（往后会说明字符串、数组等操作）


list1 = [5, 4, 3, 2, 1]
bubble_sort(list1)
