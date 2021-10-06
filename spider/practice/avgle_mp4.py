# https://static-clst.avgle.com/videos/tmb18/583452/preview.mp4
# pip install moviepy
import requests
from lxml import etree
import moviepy.editor as mpy

url = "https://avgle.com/videos"
mp4_url = "https://static-clst.avgle.com/videos/tmb18/{id}/preview.mp4"
params = {
    "o": "tr",
    "page": 2
}
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
}
resp = requests.get(url=url, params=params, headers=headers)
tree = etree.HTML(resp.text)
lis = tree.xpath("/html/body/div[6]/div[1]/div[2]/div[1]/div[3]/div/div")
for li in lis:
    template = "id:{0},img:{1},name:{2}"
    img = str(li.xpath("./a/div/img/@data-original")[0])
    id = str(img.split("/")[-2])
    name = str(li.xpath("./a/span/text()")[0])
    template = template.format(id, img, name)
    mp4_req_url = mp4_url.format(id=id)
    mp4_resp = requests.get(url=mp4_req_url, headers=headers)
    mp4_name = "mp4/" + id + ".mp4"
    print(mp4_name)
    with open(mp4_name, mode="wb") as f:
        f.write(mp4_resp.content)
        print(template)
    mp4_resp.close()
resp.close()

#
# #mv4 -> gif
# # content = mpy.VideoFileClip("mp4.mp4")
# # change = content.subclip().resize((240,120))
# # change.write_gif("mp4.gif")
#
# resp.close()
