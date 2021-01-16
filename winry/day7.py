"""
爱德华老师学堂7：只要看完今天就是一周啦~ congratulations
感觉到自己的力量涌现出来了吗？
以后见到python题还会懊恼吗？
肯定不会    (ง •_•)ง
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
用0~9这10个数字可以组成多少个能被15整除且无重复数字的三位数个数？

A：
这道题跟day6第二道题很像，但有一点细微的差异，首先是多了0，而0是不能作为数字开头的
其次要能被15整除，仅仅是条件多了一个而已，适合把day6的第二道题目拷下来 (ง •_•)ง
其实还可以遍历100~999之间的数，然后先判断是否能被15整除，然后再判断数字是否重复
"""
def match_diff_num_pro(list_num):
    match_list = []     # 定义一个空数组，为了最后统计符合条件的数有多少个，顺便可以打印出来瞧瞧 =。=
    for e1 in list_num:     # 数组完全遍历一次，取出第一个数，都是使用数组遍历，忘记可以看day3的for循环要点
        if e1 == 0:     # 0是不能作为数字开头的
            continue    # 所以碰到0赶紧撤了吧，下一轮
        for e2 in list_num:     # 数组再次遍历，再取出第二个数
            for e3 in list_num:     # 数组再次遍历，再取出第三个数
                if e1 != e2 != e3 and e1 != e3:     # day6注释2
                    match_num = int(str(e1) + str(e2) + str(e3))    # day6注释3
                    if match_num % 15 == 0:     # 取余为0
                        # print("符合规则的数字是：%d" % match_num)
                        match_list.append(match_num)    # 把符合规则的数字放入列表里
    else:
        print("pro版本：符合规则的数字列表是：%s" % str(match_list))    # 这两步都是打印结果了
        print("pro版本：符合规则的数字列表长度：%d" % len(match_list))
        return len(match_list)

match_diff_num_pro([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

"""
Q：
计算 s = 1 + 22 + 333 + 4444 + ... + 666666 的和

A：
其实就这题目，我一看就想直接手动算出来 （。＾▽＾） 毕竟只是计算到6而已，如果这么做可以过的话那也太混了吧
所以还是给了一个通用的方案出来 =。= 这样无论范围给多大都可以做了 (￣y▽,￣)╭ 

题目思路是，先把这道题看作是 1 + 2 + 3 + 4 + ... + 6，然后每次累加的时候，遍历当前累加的数字n，
n=2时遍历2次，n=3时遍历三次，然后把数字合成字符串，再把字符串转为数字

"""
def sum_up_cond_num(scope):
    sum_up = 0      # 定义和
    content = ""    # 仅仅是显示给你看
    for i in range(1, scope):   # 到scope-1为止，先把这道题看作是 1 + 2 + 3 + 4 + ... + 6
        elem_temp = ""      # 如何把2变为22，3变为333呢？
        for j in range(i):      # 把当前下标进行遍历，当前下标是2时则遍历2次，3则3次，至于j，直接不管 (。・∀・)ノ
            elem_temp += str(i)     # 字符串相加，则 i = 2时 elem_temp = '2' + '2', i = 3时 elem_temp = '3' + '3' + '3'
        content += "%s + " % elem_temp
        sum_up += int(elem_temp)    # 得到想要的数字字符串后，把它转换为数字，并累加
    else:
        print("s = %s = %d" % (content[0:-2], sum_up))
        print("和为 ：%d" % sum_up)

def sum_up_cond_num_two():      # 非常讨巧的做法，题目要啥我做啥 hhh
    sum_up = 1 + 22 + 333 + 4444 + 55555 + 666666
    print("和为 ：%d" % sum_up)
    return sum_up

sum_up_cond_num(7)
sum_up_cond_num_two()