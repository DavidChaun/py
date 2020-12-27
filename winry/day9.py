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
求出两位数内十位数比个位数大的数字之和

A：
总觉得跟day8第二题好像啊，那就以上一题的另一种做法做吧 (ง •_•)ง
"""
def sum_up_num(scope):
    sum_up = 0
    show_list = []  # 来吧，展示
    for i in range(scope):  # 遍历scope范围
        if 10 <= i < 100:   # 设定i要大于等于10小于100，才能往下走
            single_num = i % 10     # 取余10，得到个位的余数
            # ten_num = int(i / 10)   # 除以10，得到十位，但是除以算出来的是浮点数，比如 22 / 10 = 2.2，即使十位不比个位大，但是不符合要求，所以要把浮点数后面部分去除，取整
            ten_num = i // 10   # 整除10，就是除以10然后取整
            if ten_num > single_num:    # 十位大于个位
                sum_up += i     # 累加和
                show_list.append(i)     # 数组塞一个
    else:
        print("两位数内十位数比个位数大的数字：%s" % str(show_list))
        print("两位数内十位数比个位数大的数字之和：%d" % sum_up)
    return sum_up   # 题目要求和，记得返回给它 =。=

sum_up_num(100)

"""
Q：
给一个三位数，求三位数之和

A：
这题目，我看咋这么眼熟 （⊙ｏ⊙）才发现是day8第一题的变种、简易版本，可以自己思考下，差不多题型，不浪费你时间啦
顺延走起 >.<

Q：
一个三位整数，它的百位数字，十位数字，个位数字相加起来为17。满足这个条件的正整数的和为？

A：
因为三位数范围过小，所以直接以100~999为范围
当然也可以把这个三位整数看作是一个字符串，字符串的比较，也是做简单粗暴的想法 d=====(￣▽￣*)b
"""
def sum_cond_num():
    show_list = []
    sum_up = 0
    for i in range(100, 1000):
        single_num = i % 10     # 个位，取余10得出的余数
        # ten_num = int(i % 100 / 10)      # 十位，取余100得出两位数余数，再整除10得出十位的浮点数，然后取整
        ten_num = i % 100 // 10      # 十位，取余100得出两位数余数，再整除10得出十位的浮点数，然后取整
        # ten_num = int(i / 10 % 10)      # 十位，或者除以10得出两位数的浮点数，再整除10得出两位数的个位数的浮点数，然后取整
        hundred_num = i // 100  # 百位，除以100然后取整
        if single_num + ten_num + hundred_num == 17:
            show_list.append(i)
            sum_up += i
    else:
        print("符合规则的数字列表是：%s" % str(show_list))  # 这两步都是打印结果了
        print("符合规则的数字之和：%d" % sum_up)

sum_cond_num()