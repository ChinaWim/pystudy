# https://music.163.com/#/discover/playlist/?cat=%E6%97%A5%E8%AF%AD
# child_href = /html/body/div[3]/div/ul/li[1]/div/a
import requests
from lxml import etree
import time

url = "https://music.163.com/discover/playlist"
detail = "https://music.163.com"
params = {
    "order": "hot",
    "cat": "日语",
    "limit": "35",
    "offset": "0"
}
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
}


def format_filename(img):
    file_prefix = "./img/"
    file_name = str(img)
    file_name = file_name[0:file_name.find("?")]
    return file_prefix + file_name.split("/")[-1]


resp = requests.get(url=url, params=params, headers=headers)
tree = etree.HTML(resp.text)
link_list = tree.xpath("/html/body/div[3]/div/ul/li/div/a/@href")
for link in link_list:
    detail_url = detail + link
    detail_resp = requests.get(url=detail_url, headers=headers)
    detail_tree = etree.HTML(detail_resp.text)
    img = detail_tree.xpath("/html/body/div[3]/div[1]/div/div/div[1]/div[1]/img/@src")[0]
    file_name = format_filename(img)
    detail_resp.close()
    with open(file_name, mode="wb") as f:
        img_resp = requests.get(url=img)
        f.write(img_resp.content)  # content 是字节
        time.sleep(0.5)
        print("over!")
resp.close()
print("all over!!!")
