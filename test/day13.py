# import this   # python这门语言的禅道，可以打开注释看看 :P 加上#号就是注释一行代码
print("============ let's get started ============")
# ============ let's get started ============

print("============ finish ============")

"""
Q：
计算并输出下面级数前n项（n=20）中奇数项的和。
1*2*3 - 2*3*4 + 3*4*5 + ... + (-1)^(n-1)*n*(n+1)*(n+2) + ... （其中，^表示幂运算）
"""
def calc_special(n):
    sum_up = 0
    content = ""
    for i in range(1, n + 1):   # 题目是从1到n，因此[1, n+1)
        sum_up += (-1)**(i-1) * i * (i+1) * (i+2)   # **就是进行幂运算的符号，还记得吗
        content += "(-1)^(%d)*%d*%d*%d + " % ((i-1), i, (i+1), (i+2))
    else:
        print("列表公式：P = %s = %s" % (content[0:-3], str(sum_up)))
        print("P的值为：%s" % (str(sum_up)))
        return sum_up

calc_special(20)

"""
Q：
设n=20，计算输出s(n)的值，要求结果保留5位小数
s(n) = (1*2)/(3*4) + (3*4)/(5*6) + (5*6)/(7*8) + ... + [(2n-1)*2n]/[(2n+1)*(2n+2)] + ...
"""
def calc_list(n):
    sum_up = 0
    content = ""
    for i in range(1, n+1):
        sum_up += (2*i-1)*(2*i)/(2*i+1)*(2*i+2)
        content += "(%d*%d)/(%d*%d) + " % ((2*i-1), (2*i), (2*i+1), (2*i+2))
    else:
        sum_up = round(sum_up, 5)   # round(浮点数, 保留位数) 这个函数可以确定浮点数保留几位小数
        print("列表公式：s(n) = %s = %s" % (content[0:-3], str(sum_up)))
        print("s(n)的值为：%s" % (str(sum_up)))
        return sum_up

calc_list(20)