list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list2.sort()

list1.append("hello py")    # java list add
list1.remove("hello py")    # java list remove
del list1[2]                # 针对索引删除
print(list1.count(2000))    # 元素出现次数

# 内置方法
print(len(list1))           # list 长度
print(max(list2))           # list 最大最小，仅限数字list
print(min(list2))

# 支持 列表间的 + * in （同contain）

# 截取
listA = list1[1:]

# list1.    查看方法看注释吧
list1.pop()
list1.pop(1)

# 迭代
for elem in list1:
    pass
