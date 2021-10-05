# 思路
# 拿到页面源代码 requests
# 通过re 提取想要的有效信息 re

# 任务1：名字、评分、评价
import requests
import re
import csv

url = "https://movie.douban.com/chart"

he = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/94.0.4606.61 Safari/537.36 "
}

# 存入文件 csv
f = open("../res/豆瓣.csv", mode="w")
cv = csv.writer(f)

r = re.compile(r'<div class="pl2">.*?<a href=".*?">(?P<name>.*?)/ <span style="font-size:13px;">.*?</a>', re.S)
resp = requests.get(url=url, headers=he)
it = r.finditer(resp.text)
for i in it:
    dic = i.groupdict()
    dic['name'] = dic['name'].strip()
    cv.writerow(dic.values())
f.close()
resp.close()
