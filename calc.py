# 运算符，基础的同java相似
# 幂 - 返回x的y次幂
print(2 ** 3)  # 8
# 取整除 - 返回商的整数部分（向下取整）
print(-9 // 2)  # -5
print("注意啊，字符串不能+字符串以外的值")

# 比较符，java相似

# 赋值运算符，py的运算符+比较符  **=  //=
print("注意啊，没有++ --运算符")

# 位运算符，java类似 & | ^ <<

# 逻辑运算符
print("=============逻辑运算符=============")
"""
and : a and b 如果 x 为 False 或者 0，x and y 返回 False 或者 0，否则它返回 y 的计算值。 同java &&符号
or  : a or b  如果 x 不是 False 或者 0，它返回 x 的值，否则它返回 y 的计算值。 同java ||符号
not : not()   同java !符号
"""
a = 1
b = -113
if a and b:
    print("a b true")
else:
    print("a false")
print(a or b)

# 成员运算符
print("=============成员运算符=============")
"""
in : 如果在指定的序列中找到值返回 True，否则返回 False。
not in : 
"""
tuple = (3, 4, 1)
print(3 in tuple)  # True
print(233 in tuple)  # False

# 身份运算符
print("=============身份运算符=============")
"""
is : 类似==，对象比较时会比较内存地址，==在对象比较时是比较值
is not : 类似!=
"""
la = [1, 2, 3]
lb = la
print(la == lb)
print(la is lb)
lb = la[:]
print(lb)
print(la == lb)
print(la is lb)

# 字符的运算符优先级最低  is is not in not in not and or
