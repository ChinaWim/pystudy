# 1. 找到未加密的参数
# 2. 想办法把参数进行加密（参考网易的逻辑）param,encSecKey
# 3. 请求到网易，拿到评论信息
# 4.需要安装pycrypto pip install -i https://mirrors.aliyun.com/pypi/simple/ pycrypto

from Crypto.Cipher import AES
from base64 import b64encode
import json
import requests

# window.asrsea(JSON.stringify(i7b), bva4e(["流泪", "强"]), bva4e(Tu9l.md), bva4e(["爱心", "女孩", "惊恐", "大笑"]));

# 处理加密过程

d = {
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_29810786",
    "threadId": "R_SO_4_29810786"
}
e = '010001'
f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7',
g = '0CoJUm6Qyw8W8jud'
i = "LYxTafTfQKijGrpu"


def getSecKey():
    return "9beae4495631377ee73b8b5c97dff807f61b91a8a8eca14d5bd8d64800551b7850e651c801c7854d7334992d14f05cb7b039e10e5a339c2af59e12b510e623cce8f477206caf979b8f864dd77eceb21c181860d18162ce0bbefe4a259831bd24341710f2c2528a080b45fb4fd1c4e119e49c13c07ee73c2082f8cda7fbdd1185 "


def encParams(d, key):  # 加密过程
    iv = "0102030405060708"
    d = to16(d)
    aes = AES.new(key=key.encode("utf-8"), IV=iv.encode("utf-8"), mode=AES.MODE_CBC)
    bs = aes.encrypt(d.encode("utf-8"))  # 加密,加密的内容长度必须是16的倍数
    return str(b64encode(bs), "utf-8")  # 转化成字符串返回


def getParams(d):  # 默认这里接收到的是字符串
    enc1 = encParams(d, g)
    enc2 = encParams(enc1, i)
    return enc2


def to16(d):
    pad = 16 - len(d) % 16
    d += chr(pad) * pad
    return d


url = "https://music.163.com/weapi/comment/resource/comments/get"
data = {
    "referer": "https://music.163.com/song?id=29810786",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "params": getParams(json.dumps(d)),
    "encSecKey": getSecKey()
}
resp = requests.post(url=url, data=data)
print(resp.text)
