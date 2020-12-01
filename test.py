import this

def strToBin(numStr1, numStr2):
    return bin(int(numStr1, 2)+int(numStr2, 2))[2:]


a = "110"   # 6
b = "1101"  # 13
c = strToBin(a, b)  # 10011 -> 19
print(c)
