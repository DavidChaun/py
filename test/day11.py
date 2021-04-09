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
计算 sum = 1/2! + 1/4! + 1/6! + ... + 1/10!
"""
def sum_up_fatorial_step(scope=11):
    sum_up = 0  # 题目的需要的求和
    content = ""  # 展示的表达式
    for i in range(2, scope, 2):  # 遍历scope范围，题目从2开始，遍历的步长为2
        temp_num = 1  # 计算每一项的值，因为每一项的值都需要遍历，所以先设定一个中间值
        temp_content = ""  # 每个项的展示啦
        for num in range(1, i + 1):  # 因为阶乘要从1乘到i，所以范围要取到i+1才能累乘到i
            temp_num *= num  # 累乘
            temp_content += "%d*" % num  # 对应展示的串串也要叠起来
        content += "1/%s + " % temp_content[0:-1]  # 把每一项的串串串到表达式当中
        sum_up += 1 / temp_num  # 再把每一项累乘后的值累加起来~
    else:
        print("列表公式：P = %s = %s" % (content[0:-3], str(sum_up)))
        print("P的值为：%s" % (str(sum_up)))
        return sum_up


sum_up_fatorial_step(11)

"""
Q：
随机输出一个位于[0,100]的整数
"""
import random
def random_num(begin=0, end=100):
    return random.randint(0, 100)
    """
    随机输出0 - 100的整数，这个api注释是
    Return random integer in range [a, b], including both end points.
    也就是说会返回头尾两端
    """


print(random_num())




