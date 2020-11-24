# int float sting 无long（py3）
numInt = 12
a, b, c = 1, 3.1415926, "baby"
# 删除引用
del numInt, a
# print(a) 会报错

print("=============string=============")
_str = "hello jaccy"
# 截取字符串，正索引，不取最后索引值
print(_str[6:11])
# 截取字符串，负索引
print("reverse index: " + _str[-5:-1])

print("=============list=============")
_list = ['a', 'b', 'c']
# 集合取元素
print("list: " + str(_list[0:1]))
print("list: " + _list[-2:-1].__str__())
_list[1] = "bb"
print(_list)

# 元组，数组类似，元素不可变
print("=============tuple=============")
_tuple = (1, 2, 3)
try:
    _tuple[1] = 22
except:
    print("error by tuple change")

# 字典 类似java的map，kv
print("=============dict=============")
_dict = {"name": "jacy", "age": 18, "tuple": _tuple}
_dict[69] = "96"

print(_dict["name"])
print(_dict["tuple"])
print(_dict[69])

print("=============函数: 类型转换=============")
# 。。。。。
