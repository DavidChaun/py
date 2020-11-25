# 在需要在字符中使用特殊字符时，python 用反斜杠 \ 转义字符
# 普通的如同java，记录下特殊的

a = "hello"

print(a * 2)  # 字符串也能*，服气

print(a[1])  # e

print(a[1:3])  # 索引1到3，不包含3

print("l" in a)  # True，同java contain
print("l" not in a)  # False，同java contain

# 不能转义的字符串 r/R
print(R"\r\n\"\"")  # \r\n\"\"
print("\r\n\"\"")  # 空行输出 ""

# 字符串格式化 %
# %s 字符串，%d 整数，%f 浮点数
# % 后的辅助符：+显示数值正负符号
print("%s苦短，我学 %s %+d" % ("人生", "python", -3.9))  # 人生苦短，我学 python 3 （d被截断了）

# 三引号可以原样输出字符串，不用转义
javaCode = '''
        for (int j = 0; j < i; j++) {
            executor.execute(() -> {
                ChannelCallback<Object> callback = new ChannelCallback<Object>() {
                    @Override
                    public Object doInRabbit(Channel channel) throws Exception {
                        return "";
                    }
                };
                myAmqpTemplate.execute(callback);
            });
        }
'''

print("============字符串基本功能============")

b = "python"
print(b.capitalize())  # Python 首位大写
print(b.center(11))  #    python
print(b.count("y"))  # 1
print(b.count("y", 2, 5))  # 从索引2到5里y的次数
# 方法太多，直接看源码注释吧
# b.
