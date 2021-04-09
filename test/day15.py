# import this   # python这门语言的禅道，可以打开注释看看 :P 加上#号就是注释一行代码
print("============ let's get started ============")
# ============ let's get started ============

print("============ finish ============")

"""
Q：
编写一段代码，求给定的一个圆的周长和面积。要求：
（1）圆的半径r利用input函数从键盘任意输入（r>0)
（2）圆周率定义为符号常量
（3）利用赋值语句将求出的周长和面积赋值给变量L和s
（4）用print方法输出详细结果

"""
def circle():
    r = input("请输入圆的半径r：")
    pi = "Π"
    print("圆的周长为：L = %s" % (str(int(r)*2) + pi))
    print("圆的面积为：s = %s" % (str(int(r)**2) + pi))

circle()

"""
Q：
计算数学表达式 1 - 2/2! + 3/3! - 4/4! + ... + (-1)^(n+1)*n/n! 的程序

"""
def sum_step_multiply(num):
    sum_up = 0
    for i in range(1, num + 1):
        step_temp = 1
        for j in range(1, i+1):
            step_temp *= j
        sum_up += (-1)**(i+1)*i/step_temp
    return sum_up

