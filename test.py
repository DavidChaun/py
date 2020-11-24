
def strToBin(numStr1, numStr2):
    return bin(int(numStr1, 2)+int(numStr2, 2))


a = "11"
b = "1"
c = strToBin(a, b)
print(c)
