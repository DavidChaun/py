"""
爱德华老师学堂9：

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
求100~300之间的所有素数

A：
day6第一题差不多 (ง •_•)ง

Q：
计算1~9999内能被13整除的个数

A：
过于简单 =。= 遍历然后每个数取余是否为0，为0就计数器叠加上去

Q：
求表达式 1^2 + 2^2 + 3^2 + ... + 20^2的值

A：
其实也很简单，遍历到20，然后每个数都平方（9 == 3 ** 2），然后累加起来

Q：
求表达式 1^1 + 2^2 + 3^3 + ... + 8^8的值

A：
跟上一题差不多，遍历到8，然后每个数都取幂（num == i ** i），然后累加起来

Q：
求表达式 1/1^1 + 1/2^2 + 1/3^3 + ... + 1/10^10的值

A：
上面三题的糅合版 (～￣▽￣)～ 还是解一下吧
"""
def sum_up_num(scope):
    sum_up = 0  # 题目的需要的求和
    content = ""    # 展示
    for i in range(1, scope):  # 遍历scope范围，题目从1开始的
        sum_up += 1 / i ** i    # 题目就是 1 除以 i 的 i 次方的值直接累加起来
        content += "1/%d^%d + " % (i, i)    # 使用数字替换符，替换字符串的%d
    else:
        print("列表公式：%s = %s" % (content[0:-3], str(sum_up)))
        print("返回值，和为 sum_up = %s" % (str(sum_up)))
    return sum_up  # 题目要求和，记得返回给它 =。=


sum_up_num(11)

"""
Q：
求表达式 1 + 3 + 5 + ... + 99

A：
过于简单 =。= 直接循环到100（不包含100的记得吧），并设置步长为2（步长可以看第5天第一题~~），从1开始就 ooook

Q：
求P的值，P = 1! + 2! + 3! + ... + 9!

A：
阶乘n!，只要概念没忘，题目就能写出来 hiahiahia，就是每一项都是从1到当前项的数字的累乘的值 (ง •_•)ง
"""
def sum_fatorial_num(scope=10):
    sum_up = 0  # 题目的需要的求和
    content = ""    # 展示的表达式
    for i in range(1, scope):   # 遍历scope范围，题目从1开始
        temp_num = 1    # 计算每一项的值，因为每一项的值都需要遍历，所以先设定一个中间值
        temp_content = ""   # 每个项的展示啦
        for num in range(1, i + 1):     # 因为阶乘要从1乘到i，所以范围要取到i+1才能累乘到i
            temp_num *= num     # 累乘
            temp_content += "%d*" % num     # 对应展示的串串也要叠起来
        content += "%s + " % temp_content[0:-1]     # 把每一项的串串串到表达式当中
        sum_up += temp_num      # 再把每一项累乘后的值累加起来~
    else:
        print("列表公式：P = %s = %s" % (content[0:-3], str(sum_up)))
        print("P的值为：%s" % (str(sum_up)))
        return sum_up

sum_fatorial_num(10)












