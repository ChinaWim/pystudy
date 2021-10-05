import requests

url = 'https://movie.douban.com/j/chart/top_list'


param = {
    "type": 15,
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "20"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/94.0.4606.61 Safari/537.36 "
}
resp = requests.get(url=url, params=param, headers=headers)
print(resp.request.url)
print(resp.json())
