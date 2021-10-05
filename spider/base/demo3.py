import requests

url = "https://fanyi.baidu.com/sug"
s = input("请输入你要翻译的英文单词")
dic = {
    "kw": s
}
resp = requests.post(url, data=dic)
print(resp.json())
resp.close()