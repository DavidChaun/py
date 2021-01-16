"""
爱德华老师学堂11：
2021.01.04
今天用python写了些小工具给运营同事，写完交付后同事眼睛都发光了 (～￣▽￣)～
看来我这样学学python，还能帮到人还是挺开心的 hhh

都快将注释写成日记了（正经人谁写日记啊），很奇怪的感觉

现在都习惯晚上8点下班了，晚点回宿舍，学点东西
毕竟不想一下班回去就看到舍友在玩游戏，这也太颓了
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
输出1到100自然数中被7整除的数据的个数及他们的和

A：
遍历1到100，然后每个数除以7取余为0时，累加值，并且计数器+1
前面有类似的题目啦，如果想知道答案话回馈我就行

Q：
输入长方形的长和宽，计算长方形的面积，并输出

A：
众所周知，长方形的面积 = 长 * 宽 。。。没什么难度

Q：
输入圆的半径，计算圆的周长，并输出。

A：
同上。。圆的周长 = 半径 * 2 * Π，当然Π没办法具体取值，所以一般也是取3.14作为计算

Q：
计算 sum = 1/2! + 1/4! + 1/6! + ... + 1/10!

A：
发现了吗？跟第10天的第二道题差不多的，但是遍历的时候步长变了，我还是解一下吧~~

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
计算sum = 1 + 3 + 5 + ... + 99

A：
循环累加，步长为2，你懂的~

Q：
随机输出一个位于[0,100]的整数

A：
这个就是直接调用随机数的API了，我简单写一下哈
需要导入random包，一般导包会放在文件开头，为了方便看我放到方法上面了 hhh

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




