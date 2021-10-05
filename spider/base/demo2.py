# 安装requests
import requests

url = 'https://www.baidu.com/s?wd=周杰伦'
# User-Agent:
dic = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/94.0.4606.61 Safari/537.36 "
}
resp = requests.get(url, headers=dic)
print(resp.text)  # 拿到页面源代码
