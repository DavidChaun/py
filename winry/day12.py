"""
爱德华老师学堂12：
2021.01.05 - 2020.01.06

最近加班有点多，白天工作多了点 =。= 可能年末了，都这样
本来想重制第七天的内容，后来发现，其实没多少能改动的？？ （⊙ｏ⊙） 后来想想还是没发了
如果还是想不通的话还是问我吧 hhh

最近我的舍友终于开窍了，准备开始找工作了 =。= 应该是身上没什么钱了，祝他好运吧

想你
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
编写一个函数，求两个数的最小数。

A：
感觉完全没必要做出来啊。。直接使用python的自带函数 min(a, b)，会返回其中小的一个

Q：
输入一个四位数，分别输出它的个位数字、十位数字、百位数字、千位数字

A：
有两种想法。 (ง •_•)ง
第一种是把四位数变成字符串，然后输出字符串的第四位、第三位、第二位、第一位；比较简单
第二种是用数学的做法，对10取余得到个位数，对100取余然后整除10得到十位数，对1000取余然后整除100得到百位数，对1000整除得到千位数
下面给你列两种想法 ~ ~
"""
def find_num_one(num):
    if num < 1000 or num > 9999:    # 我很尊重的一个人说过，不要相信任何第三方 =。= 所以就算是传值，也校验一下是不是四位数，不是的话就让它滚蛋 _〆(´Д｀ )
        return

    num_str = str(num)      # 数字转为字符串
    print("个位数：%s；十位数：%s；百位数：%s；千位数：%s" %       # 取第四位、第三位、第二位、第一位作为个位、十位、百位、千位
          (num_str[3], num_str[2], num_str[1], num_str[0]))     # 字符串       1874
                                                                # 对应索引     0123

def find_num_two(num):
    if num < 1000 or num > 9999:    # 校验，同上了
        return

    print("个位数：%d；十位数：%d；百位数：%d；千位数：%d" %       # 对10取余得到个位数，对100取余然后整除10得到十位数，对1000取余然后整除100得到百位数，对1000整除得到千位数
          (num % 10, num % 100 // 10, num % 1000 // 100, num // 1000))


find_num_one(1874)
find_num_two(1874)

"""
Q：
随机输出一个小（大）写字母

A：
也有两种想法~~
对于我这种计算机基础不太熟悉的小伙汁，先把所有大小写字母列到一个数组里面，然后取数据长度范围的随机数，然后取随机数索引对应的元素；

第二种是获取ASCII码，这个要知道大写到小写对应的ASCII码的范围，取范围内的值就行
65 - 90 是大写字母，97 - 122 是小写字母
下面可看ASCII码的范围 ~ ~
https://baike.baidu.com/pic/ASCII/309296/1/e850352ac65c103880a07b53bc119313b17e8941?fr=lemma&ct=single#aid=1&pic=e850352ac65c103880a07b53bc119313b17e8941
然后随机获取 65 - 90 and 97 - 122 范围内的数字，使用chr(数字)得到对应字母

"""

import random       # 随机数的包
def random_alphabet_one():
    alphabet_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'       # 所有的大小写字母
    index = random.randint(0, len(alphabet_str) - 1)        # 获取随机数，0 ~ 51，对应alphabet_str的字符的索引
    return alphabet_str[index]      # 根据索引从字符串取出字符

def random_alphabet_two():
    ascii_code = random.randint(65, 122)    # 获取65 - 122之间的随机数
    while 90 < ascii_code < 97:     # 如果得到的随机数在90 - 97之间，则进入循环重新获取随机数，因为90 - 97之间的ASCII编码不是英文字母
        ascii_code = random.randint(65, 122)    # 再次获取65 - 122之间的随机数，除非触发了终止条件，获取的随机数不在90 - 97之间
    return chr(ascii_code)      # chr(ascii编码)  可以把编码变成字符


print(random_alphabet_one())
print(random_alphabet_two())
