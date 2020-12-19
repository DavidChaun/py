# if
if 1 == 1 and 2 == 2:
    print("1 = 1")
elif 1 == 2:
    print("impossible")
else:
    pass  # 空语句

# while
_count = 0
while _count < 5:
    _count += 1
    if _count == 2:
        continue
    print("cycling, count = " + str(_count))
    if _count == 6:
        break
else:  # 不符合判断条件时，执行else，当循环被break，不会执行else
    print("cycle ending. count = " + str(_count))

# for 基本同while
_list = [31, 22, 3, 41, 88]
# 增强for循环
for num in _list:
    pass
else:  # 循环完执行else。当循环被break，不会执行else
    print("list 之后打印")


# 嵌套循环，来个冒泡，索引迭代，从小到大
# 冒泡算法
def bubble(_list):
    # _count = _list.__len__()
    size = len(_list)
    for i in range(size):
        # 此处的j为循环外变量
        # j = i + 1
        # for j in range(_count):
        for j in range(i + 1, size):
            # 此处的j为循环内变量，因此并不互通
            # print(str(_list[i]) + " : " + str(_list[j]))
            if _list[i] > _list[j]:
                _list[i], _list[j] = _list[j], _list[i]
    else:
        print(_list)


bubble(_list)

