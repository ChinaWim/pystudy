# 代理目的是为了防止短时间内请求多次网站，ip被封
# 1.找一个能代理的ip 如：站大爷网站里找
import requests

proxies = {
    "https": "https://218.60.8.83:3129",
}
resp = requests.get("https://www.baidu.com", proxies=proxies)
resp.encoding = "utf-8"
print(resp.text)
