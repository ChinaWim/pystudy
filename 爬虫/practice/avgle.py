#
import requests
import re
import csv

#, verify=False
def spider(param, url):
    header = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/94.0.4606.61 Safari/537.36 "
    }
    resp = requests.get(url=url, params=param, headers=header)
    obj1 = re.compile(r'<div class="well well-sm">.*?'
                      r'<a href="(?P<url>.*?)".*?'
                      r'<div class="duration">(?P<duration>.*?)</div>.*?'
                      r'<span class="video-title title-truncate m-t-5">(?P<title>.*?)</span>.*?'
                      r'<div class="video-added">(?P<added>.*?)</div>.*?'
                      r'<div class="video-views pull-left">(?P<views>.*?)<i class="glyphicon glyphicon-play-circle">.*?'
                      r'<i class="fa fa-heart video-rating-heart "></i> <b>(?P<heart>.*?)</b>', re.S)
    it = obj1.finditer(resp.text)

    domain = "https://avgle.com"

    f = open("../res/avgle.csv", mode="a+")
    cv = csv.writer(f)
    cv.writerow(['url', 'duration', 'title', 'added', 'views', 'heart'])
    for i in it:
        dic = i.groupdict()
        dic['url'] = domain + dic['url'].strip()
        dic['duration'] = dic['duration'].strip()
        dic['title'] = dic['title'].strip()
        dic['added'] = dic['added'].strip()
        dic['views'] = dic['views'].strip()
        dic['heart'] = dic['heart'].strip()
        cv.writerow(dic.values())
    f.close()
    resp.close()
    return


param = {
    "o": "tr",
    "page": "2"
}

url = "https://avgle.com/videos"

length = int(input("请输入要爬的页数："))
for i in range(1, length):
    param = {
    "o": "tr",
    "page": i
    }
    spider(param, url)

