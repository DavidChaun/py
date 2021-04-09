import builtwith
import whois
from urllib import robotparser

url = "https://docs.qq.com/sheet/DZmZTUUNLZGRBV05T?tab=BB08J2"
content = builtwith.parse(url)
print(content)
# author = whois.whois(url)
# print(author)

parser = robotparser.RobotFileParser("https://www.taobao.com/robots.txt")
parser.read()
# allow_operate = parser.can_fetch("Baiduspider", "http://www.taobao.com/article")
allow_operate = parser.can_fetch("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36", "http://www.taobao.com/article")
print(allow_operate)