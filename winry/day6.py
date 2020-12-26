"""
爱德华老师学堂6：今天的内容是两道题目，顺便一提，题目都是摘自https://www.taodocs.com/p-390634479.html
也就是当时你告诉我考试类似的题目，摘自《信息技术教师招聘编程题目及答案解析.doc_淘豆网》
我发现我挺多题目都没有写返回值，如果题目明确需要返回值，记得return回去

圣诞快乐~与你很开心 20201225-20201226
"""
# import this   # python这门语言的禅道，可以打开注释看看 :P 加上#号就是注释一行代码
import math

print("============ let's get started ============")
# ============ let's get started ============

print("============ finish ============")

"""
每日答疑时间 =。=
因为没有基础语法教了，只能讲解题目了hhh
"""

"""
前一天顺延下来的题，题目看不懂，应该是有图案的，但是没显示出来，我猜不了=。=
所以继续顺延下一道~~
判断一个数字，如果是质数，则显示质数；如果是合数，则显示它的因数积的形式，例如6显示为3*2

思路：质数只有1和它本身可以被整除，因此最基础的想法就是把数字num从2开始到num-1，看是否可以被整除
当然还有缩短算法时间的做法~~
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

separate_num(1003471)

"""
for factor in range(2, int(math.sqrt(num)) + 1):    # 注释1
math.sqrt(num) 取num的平方根，返回浮点数float
int(num) 取num的整数部分
整句话的意思就是，取num的平方根，向上取整，为什么遍历2到num的平方根就可以了呢？下面说一下
我们假设num为16
如果把数字num从2开始到num-1，则遍历的时候会是这样
2   3   4   5   ... 14  15
当我们跑到5的时候，5往后乘以的任何数能得到16，都在5以前出现过了

而平方根算是一个数的因数的中位数，4是16的中位因子，再往下得出合数结果时，比如取到8时，与2相乘可以得到16，但是2在一开始就得出了另一个因子是8
2   3   4

所以只算到平方根是可以大大缩短算法时间

当然解释得可能不太通俗。。看多两边？？  ╮(￣▽￣"")
"""



"""
顺延的题目是一个图形拼凑题，觉得意义不大，继续顺延   =。=
再顺延：任意输入100-999的数字，得出其个位数   -- 这也太简单了吧，不做，直接整除10就行

由1、2、3、4四个数字，能组成多少个互不相同且不重复的三位数？
初次看到，感觉就是遍历这个数组三次，每次都取出一个元素进行匹配，有相同数字的就放弃它，三个数字都不同的，放入到数组里面

    ( ´▽｀)╭ 
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
题目只是说要统计个数，其实可以不用把数字显示出来，也可以用个计数器什么的统计的；str()把数字变为字符串，那么字符串相加就是直接拼接，然后再把拼接完的字符串使用int()函数变为数字

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


"""
用0~9这10个数字可以组成多少个能被15整除且无重复数字的三位数个数？
这道题跟上一道题很像，但有一点细微的差异，首先是多了0，而0是不能作为数字开头的
其次要能被15整除，仅仅是条件多了一个而已，适合把上面的题目拷下来 (ง •_•)ง
"""
def match_diff_num_pro(list_num):
    match_list = []     # 定义一个空数组，为了最后统计符合条件的数有多少个，顺便可以打印出来瞧瞧 =。=
    for e1 in list_num:     # 数组完全遍历一次，取出第一个数，都是使用数组遍历，忘记可以看day3的for循环要点
        if e1 == 0:     # 0是不能作为数字开头的
            continue    # 所以碰到0赶紧撤了吧，下一轮
        for e2 in list_num:     # 数组再次遍历，再取出第二个数
            for e3 in list_num:     # 数组再次遍历，再取出第三个数
                if e1 != e2 != e3 and e1 != e3:     # 注释2
                    match_num = int(str(e1) + str(e2) + str(e3))    # 注释3
                    if match_num % 15 == 0:
                        # print("符合规则的数字是：%d" % match_num)
                        match_list.append(match_num)    # 把符合规则的数字放入列表里
    else:
        print("pro版本：符合规则的数字列表是：%s" % str(match_list))    # 这两步都是打印结果了
        print("pro版本：符合规则的数字列表长度：%d" % len(match_list))
        return len(match_list)

match_diff_num_pro([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

"""
计算 s = 1 + 22 + 333 + 4444 + ... + 666666 的和
其实就这题目，我一看就想直接手动算出来 （。＾▽＾） 毕竟只是计算到6而已，如果这么做可以过的话那也太混了吧
所以还是给了一个通用的方案出来 =。=
"""
def sum_up_cond_num(scope):
    sum_up = 0      # 定义和
    content = ""    # 仅仅是显示给你看
    for i in range(1, scope):   # 到scope-1为止，先把这道题看作是 1 + 2 + 3 + 4 + ... + 6
        elem_temp = ""      # 如何把2变为22，3变为333呢？
        for j in range(i):      # 把当前下标进行遍历，当前下标是2时则遍历2次，3则3次，至于j，直接不管
            elem_temp += str(i)     # 字符串相加，则 i = 2时 elem_temp = '2' + '2', i = 3时 elem_temp = '3' + '3' + '3'
        content += "%s + " % elem_temp
        sum_up += int(elem_temp)    # 得到想要的数字字符串后，把它转换为数字，并累加
    else:
        print("s = %s = %d" % (content[0:-2], sum_up))
        print("和为 ：%d" % sum_up)


sum_up_cond_num(9)


"""
顺延下来又是一到组成图形的题目，算了吧
下一题：
输入一个正整数，然后得出该数的每一位非零数字相乘的积

初看看错题目了，以为是求出正整数所有最小因数的组合
结果深入一看，这也太简单了，把数字转换为字符串，然后遍历字符串，把字符转为数字相乘即可
"""
def multiply_str(num):
    num_str = str(num)      # 把数字转为字符串，用于遍历
    multiply_result = 1     # 把乘积设为1先
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
找出所有三位数的升序数，就是个位大于十位，十位大于百位
其实还可以遍历1000以内的数，分别整除100得出个位，整除10得出十位，除以100得出百位，再比较数字 =。=
感觉这个思维比较数学一点 hhh
另一种做法你可以思考一下
我这种就是比较字符大小了
"""
def asc_num():
    # num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]      # 想了一下，百位的首位不能为0，且是最小的一位，所以直接把0去掉可以了
    size = len(num_list)    # 数组长度
    show_list = []  # 最后展示给你看的数组
    for i in range(size):   # 先从数组取出百位
        hundred_num = num_list[i]
        for j in range(i + 1, size):    # 再从剩余数组取出十位
            ten_num = num_list[j]
            for k in range(j + 1, size):    # 再从剩余数组取出个位
                single_num = num_list[k]
                if hundred_num < ten_num < single_num and hundred_num < single_num:     # 个位大于十位，十位大于百位
                    show_list.append(int(str(hundred_num) + str(ten_num) + str(single_num)))    # 放入数组里
    else:
        print("升序数：%s" % str(show_list))

asc_num()

"""
求出两位数内十位数比个位数大的数字之和
总觉得跟上一题好像啊，那就以上一题的另一种做法做吧
"""
def sum_up_num(scope):
    sum_up = 0
    show_list = []  # 来吧，展示
    for i in range(scope):  # 遍历scope范围
        if 10 <= i < 100:   # 设定i要大于等于10小于100，才能往下走
            single_num = i % 10     # 整除10，得到个位的余数
            ten_num = int(i / 10)   # 除以10，得到十位，但是除以算出来的是浮点数，比如 22 / 10 = 2.2，即使十位不比个位大，但是不符合要求，所以要把浮点数后面部分去除，取整
            if ten_num > single_num:    # 十位大于个位
                sum_up += i     # 累加和
                show_list.append(i)     # 数组塞一个
    else:
        print("两位数内十位数比个位数大的数字：%s" % str(show_list))
        print("两位数内十位数比个位数大的数字之和：%d" % sum_up)

sum_up_num(100)