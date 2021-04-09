# import this   # python这门语言的禅道，可以打开注释看看 :P 加上#号就是注释一行代码
print("============ let's get started ============")
# ============ let's get started ============

print("============ finish ============")

"""
求 1 + 1/3 + 1/5 + ... + 1/(2n - 1) 的和
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
求出 s = 1*3*5 + 2*4*6 + ... + 19*21*23 + 20*22*24
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