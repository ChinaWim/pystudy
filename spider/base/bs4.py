# 安装
# pip install -i https://mirrors.aliyun.com/pypi/simple/ bs4
#导入
import requests
from spider.base.bs4 import BeautifulSoup
#解析数据
url = "http://www.baidu.com"
resp = requests.get(url)
BeautifulSoup(resp.text,"html.parser")
#从bs对象中查找数据
#find(标签,属性值)
#find_all(标签,属性值)