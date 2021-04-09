# import this   # python这门语言的禅道，可以打开注释看看 :P 加上#号就是注释一行代码
import math
import cmath
print("============ let's get started ============")
# ============ let's get started ============

print("============ finish ============")

"""
输入两个正整数m、n，求最大公因子
如果要快速寻找，还可以加上二分法
"""
def find_greatest_common_factor(m, n):
    common_factor = min(m, n)  # 求两个数里面最小的，然后最小的数递减下去，看是否可以被两个数整除
    while common_factor >= 1:   # 其中一个数为素数的话，最大的公因子就是1了，所以循环到1的时候就终止
        if m % common_factor == 0 and n % common_factor == 0:
            break       # 当得出公因数时中断循环
        common_factor -= 1      # 因数递减
    print("%d、%d，最大公因子为 %d" % (m, n, common_factor))
    return common_factor

find_greatest_common_factor(20, 24)

"""
以1、2、3、4、5为边长可以形成多少个三角形？不考虑相同的情况，请输出这些三角形的三个边长
a + b > c 按照这个规则
分三次遍历取数组不同下标的元素
"""
def find_tri_angle(list_num):
    size = len(list_num)    # 得出数组长度，决定最外层循环的次数
    for i in range(size):   # 依次取元素，每次取出边长1
        line1 = list_num[i]     # 设下标i的为边长1
        for j in range(i + 1, size):    # 对除了i元素的剩余数组进行遍历
            line2 = list_num[j]     # 设下标j的为边长2
            for k in range(j + 1, size):    # 对除了i，j元素的剩余数组进行遍历
                line3 = list_num[k]     # 设下标k的为边长3
                if (line1 + line2 > line3) and (line1 + line3 > line2) and (line2 + line3 > line1):     # 任意两边大于第三边的python表示
                    print("边长%d, %d, %d可以组成三角形" % (line1, line2, line3))        # 字符串数字占位符

find_tri_angle([1, 2, 3, 4, 5])

