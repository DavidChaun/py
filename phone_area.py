# 元组，不可修改的数组
# -*- coding: utf-8 -*-
from __future__ import print_function

import ssl, hmac, base64, hashlib
from datetime import datetime as pydatetime

try:
    from urllib import urlencode
    from urllib2 import Request, urlopen
except ImportError:
    from urllib.parse import urlencode
    from urllib.request import Request, urlopen

# 云市场分配的密钥Id
secretId = "AKIDf3Yy99Ml1gAfFu64bictki7ui1R40PXbMkC"
# 云市场分配的密钥Key
secretKey = "697U303y0LnA1nXt8s84NJ24gAAnVLEWtTCBZ4i"
source = "market"

# 签名
datetime = pydatetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
signStr = "x-date: %s\nx-source: %s" % (datetime, source)
sign = base64.b64encode(hmac.new(secretKey.encode('utf-8'), signStr.encode('utf-8'), hashlib.sha1).digest())
auth = 'hmac id="%s", algorithm="hmac-sha1", headers="x-date x-source", signature="%s"' % (secretId, sign.decode('utf-8'))

# 请求方法
method = 'GET'
# 请求头
headers = {
    'X-Source': source,
    'X-Date': datetime,
    'Authorization': auth,
}
# 查询参数
queryParams = {
    'mobile': '1307923'}
# body参数（POST方法下存在）
bodyParams = {
}
# url参数拼接
url = 'https://service-av27cw4h-1257598706.ap-shanghai.apigateway.myqcloud.com/release/mobile'
if len(queryParams.keys()) > 0:
    url = url + '?' + urlencode(queryParams)

request = Request(url, headers=headers)
request.get_method = lambda: method
if method in ('POST', 'PUT', 'PATCH'):
    request.data = urlencode(bodyParams).encode('utf-8')
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urlopen(request, context=ctx)
content = response.read()
if content:
    print(content.decode('utf-8'))