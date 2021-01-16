# import this
import json
# import requests
import re
import time
import base64
import random
import sys

def str_to_bin(numStr1, numStr2):
    return bin(int(numStr1, 2)+int(numStr2, 2))[2:]


def read_file():
    file = open("winry/day10.py", "rt", encoding="UTF-8")
    for data in file:
        print(data, end="")

def read_json():
    json_data = '{"code":230, "msg":"key错误或为空"}'
    data = json.loads(json_data)
    dict1 = dict(data)
    print(dict1.get("code"))

def regex_test():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
                      '*', sentence, flags=re.IGNORECASE)
    print(purified)  # 你丫是*吗? 我*你大爷的. * you.

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
print(time.strftime("%Y%m%d%H%M%S", time.localtime()))

str1 = "D:/该小程序由志玮独家开发.xlsx"
base_str = str1[str1.find(":/") + 2:str1.find(".xlsx")]
a = base64.b64encode(base_str.encode("UTF-8"))
print(str(a, "UTF-8"))
print(str(base64.b64decode(a), "UTF-8"))

print(sys.version)