from math import sqrt

"""
for i in range(1, 10):
    for j in range(1, 10):
        print("%d * %d = %d" % (i, j, i * j), end="\t")
    print()
"""

def winry(num):
    sum = 0
    content = ""
    for i in range(1, num):
        sum += 1/i * 1/(i + 1) * 1/(i + 2)
        content += "1/" + str(i) + " * " + "1/" + str((i + 1)) + " * " + "1/" + str((i + 2)) + " + "
    else:
        print("和为：%s" % str(sum))
        print("列表公式：" + content)
    return sum

winry(101)


