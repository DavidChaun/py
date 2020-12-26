"""
爱德华老师学堂5：今天的内容是两道题目，顺便一提，题目都是摘自https://www.taodocs.com/p-390634479.html
也就是当时你告诉我考试类似的题目，摘自《信息技术教师招聘编程题目及答案解析.doc_淘豆网》
平安夜祝你梦想成真 20201224
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
求 1 + 1/3 + 1/5 + ... + 1/(2n - 1) 的和
又是一道经典的数列求和的题目，看数列元素的分母，是奇数，直接循环跑就行 =。=
"""
def sum_up_step(num):
    sum_up = 0     # 定义和
    content = ""    # 主要是为了显示数列给你看~
    for i in range(1, 2 * num, 2):  # 新知识：for循环的range函数，range(begin, end, step)，指从begin开始数，到end结束（不包括end），步长为step（不指定步长则默认步长为1）
        sum_up += 1 / i    # 模拟公式的分数
        content += "1/%d + " % i    # 显示而已，对结果无影响
    else:
        print("列表公式为：%s = %s" % (content[0:-2], str(sum_up)))
    return sum

sum_up_step(101)


"""
求和，求sin(x) = x/1 - x^3/3! + x^5/5! - ... (-1)^(n - 1) * x^(2 * n - 1)/(2n - 1)!
题目我没看懂，所以顺延到下一题 hhh

求出 s = 1*3*5 + 2*4*6 + ... + 19*21*23 + 20*22*24
初看题目的思路：循环到24，然后每三个数分作一组，当每组有三个数的时候，求乘积，然后把乘积加起来 =。=
后面看了答案还有种根据步长的思路，我觉得不是我一看就想得出来的，所以没写，当然你也可以写出来教我  _(:_」∠)_
"""
def sum_multiply_step(num):
    list_single = []    # 奇数数组
    list_double = []    # 偶数数组
    sum_up = 0      # 求和
    content = ""    # 记住，以后content都是对题目没有影响的，只是为了看看公式有没有错 >.<
    for i in range(1, num):     # 假设到24为止，所以要给25
        if i % 2 != 0:      # 判断当前元素是否奇数
            list_single.append(i)   # 奇数则加入到奇数数组
        else:   # 不是奇数那肯定是偶数啦
            list_double.append(i)   # 那就加入偶数数组

        if len(list_single) == 3:   # 当奇数数组有三个元素的时候
            sum_temp = list_single[0] * list_single[1] * list_single[2]     # 把它们几个都相乘起来，并放入到临时值中
            sum_up += sum_temp      # 和加上临时值，和上面的一句其实可以合并起来，做的时候没有留意
            content += "%d*%d*%d + " % (list_single[0], list_single[1], list_single[2])     # 展示看看
            list_single = []    # 当奇数数组已经满员，重新给一个新的数组对象，把旧的抛弃了 =。= 也可以使用list_single.clear(),clear会把原来的数组清空，内存值不会改变

        if len(list_double) == 3:   # 偶数的想法跟奇数的一样了 0.0
            sum_temp = list_double[0] * list_double[1] * list_double[2]
            sum_up += sum_temp
            content += "%d*%d*%d + " % (list_double[0], list_double[1], list_double[2])
            list_double = []
    else:
        print("列表公式为：%s = %s" % (content[0:-2], str(sum_up)))
        return sum_up

sum_multiply_step(25)