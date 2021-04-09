# import this   # python这门语言的禅道，可以打开注释看看 :P 加上#号就是注释一行代码
import math

print("============ let's get started ============")
# ============ let's get started ============

print("============ finish ============")

"""
Q：
判断一个数字，如果是质数，则显示质数；如果是合数，则显示它的因数积的形式，例如6显示为3*2
"""
def separate_num(num):
    is_prime = True     # 是否是质数的标记，如果一旦发现有合适的因数，就设置为false，为了到最后打印 是否是质数
    # for factor in range(2, num):    # 从2轮询到num-1，逐个试是否整除
    for factor in range(2, int(math.sqrt(num)) + 1):    # 注释1
        if num % factor == 0:   # 没有余数
            is_prime = False
            print("合数 %d = %d*%d" % (num, num / factor, factor))
    else:
        if is_prime:
            print("质数 %d" % num)
    return num

separate_num(7311700130931232465467577713)

"""
for factor in range(2, int(math.sqrt(num)) + 1):    # 注释1
math.sqrt(num) 取num的平方根，返回浮点数float
int(num) 取num的整数部分
整句话的意思就是，取num的平方根，向下取整，然后加1确定比平方根浮点数大，为什么遍历2到num的平方根就可以了呢？下面说一下
我们假设num为16
如果把数字num从2开始到num-1，则遍历的时候会是这样
2   3   4   5   ... 14  15
当我们跑到5的时候，5往后乘以的任何数如果能得到16，都在5以前出现过了

而平方根算是一个数的因数的中位数，4是16的中位因子，再往下得出合数结果时，比如取到8时，与2相乘可以得到16，但是2在一开始就得出了另一个因子是8
2   3   4

所以只算到平方根是可以大大缩短算法时间
"""



"""
Q：
由1、2、3、4四个数字，能组成多少个互不相同且不重复的三位数？
"""
def match_diff_num(list_num):
    match_list = []     # 定义一个空数组，为了最后统计符合条件的数有多少个，顺便可以打印出来瞧瞧 =。=
    for e1 in list_num:     # 数组完全遍历一次，取出第一个数，都是使用数组遍历，忘记可以看day3的for循环要点
        for e2 in list_num:     # 数组再次遍历，再取出第二个数
            for e3 in list_num:     # 数组再次遍历，再取出第三个数
                if e1 != e2 != e3 and e1 != e3:     # 注释2
                    match_num = int(str(e1) + str(e2) + str(e3))    # 注释3
                    # print("符合规则的数字是：%d" % match_num)
                    match_list.append(match_num)    # 把符合规则的数字放入列表里
    else:
        print("符合规则的数字列表是：%s" % str(match_list))    # 这两步都是打印结果了
        print("符合规则的数字列表长度：%d" % len(match_list))
        return len(match_list)

"""
注释2：
发现了一个很有意思的东西，e1 != e2 != e3，说的是e1不等于e2，e2不等于e3，但是没说e1不等于e3。。。典型的工科思维啊，所以还要再加一个条件说明e1不等于e3 hhh
注释3：
str()把数字变为字符串，那么字符串相加就是直接拼接，然后再把拼接完的字符串使用int()函数变为数字
题目只是说要统计个数，其实可以不用把数字显示出来，也可以用个计数器统计；

如果用计数器的方式，其实会节省许多时间？
def match_diff_num(list_num):
    count = 0     # 定义计数器
    for e1 in list_num:     # 数组完全遍历一次，取出第一个数，都是使用数组遍历，忘记可以看day3的for循环要点
        for e2 in list_num:     # 数组再次遍历，再取出第二个数
            for e3 in list_num:     # 数组再次遍历，再取出第三个数
                if e1 != e2 != e3 and e1 != e3:     
                    count += 1  # 发现一个符合规则的数，加1
    return count
"""

match_diff_num([1, 2, 3, 4])


