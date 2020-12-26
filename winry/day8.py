"""
爱德华老师学堂8：
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
顺延下来又是一到组成图形的题目，算了吧 o((⊙﹏⊙))o.
下一题：
Q：
输入一个正整数，然后得出该数的每一位非零数字相乘的积

A：
初看看错题目了，以为是求出正整数所有最小因数的组合 (+_+)?
结果深入一看，这也太简单了，把数字转换为字符串，然后遍历字符串，把字符转为数字相乘即可
"""
def multiply_str(num):
    num_str = str(num)      # 把数字转为字符串，用于遍历
    multiply_result = 1     # 把乘积设为1先 (ง •_•)ง
    content = "%s : " % num_str
    for e in num_str:       # 其实字符串就是字符数组，可以当成数组遍历
        if int(e) == 0:     # 判断字符转为数字时，结果是否为0
            continue        # 如果是0，跳过这次循环，进行下一次循环
        multiply_result *= int(e)   # 把字符数字相乘起来~
        content += "%d * " % int(e)
    else:
        print("%s = %d" % (content[0:-2], multiply_result))
    return multiply_result  # 返回结果值

multiply_str(1203444)


"""
Q：
找出所有三位数的升序数，就是个位大于十位，十位大于百位

A：
其实还可以遍历1000以内的数，整除100再整除10得出个位，除以10整除10得出十位，除以100得出百位，再比较数字 =。=
感觉这个思维比较数学一点 hhh
另一种做法你可以思考一下
我这种就是比较字符大小了 ε=ε=ε=(~￣▽￣)~
"""
def asc_num():
    # num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]      # 想了一下，百位的首位不能为0，且是最小的一位，所以直接把0去掉可以了
    size = len(num_list)    # 数组长度
    show_list = []  # 最后展示给你看的数组
    for i in range(size):   # 先从数组取出百位
        hundred_num = num_list[i]   # 百位数~
        for j in range(i + 1, size):    # 再从剩余数组取出十位
            ten_num = num_list[j]   # 十位数~
            for k in range(j + 1, size):    # 再从剩余数组取出个位
                single_num = num_list[k]    # 个位数
                if hundred_num < ten_num < single_num and hundred_num < single_num:     # 个位大于十位，十位大于百位 (oﾟvﾟ)ノ
                    show_list.append(int(str(hundred_num) + str(ten_num) + str(single_num)))    # 放入数组里
    else:
        print("升序数：%s" % str(show_list))

asc_num()