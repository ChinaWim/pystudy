# 1.模拟浏览器登录->处理cookie
# 2.防盗链处理->抓取梨视频数据
# 3.代理->防止被封ip
# 任务：
#    抓取网易云音乐评论信息

import requests
# 1.模拟浏览器登录

# 会话
# session = requests.session()
# url = ""
# session.post(url,data="")
# 不要使用requests.post 发起一个新的请求，要使用刚才的对象，因为要同一个session
# session.get()
import requests
from lxml import etree

# 爬取知乎热搜评论
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "cookie": 'q_c1=8629c02e52fd40c3b668328d87737793|1613478180000|1613478180000; '
              '_xsrf=Vb8OVd8qEfE6tnU4eAPpWlBq2GQiodzH; _zap=3a8b2740-1ff6-4a2a-8a00-9678d28dc27b; '
              'd_c0="AGCYTELGqhKPTl4n3TJuFADSfC3qsdLLoII=|1613478124"; '
              'q_c1=0fffd462861d4b06a1cece4913525e53|1614519590000|1614519590000; __snaker__id=xlJVjlVEho9tcXyx; '
              '_9755xjdesxxd_=32; YD00517437729195%3AWM_TID=UffRZQop%2FclFBBRAAAd%2B2v%2BnS%2F3YlQIo; '
              'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1632041346,1633192025,1633359331,1633359632; tshl=; tst=h; '
              'gdxidpyhxdE=Wl9ULMeifJtAehN5P0ZGp4cJhar2LfmT1XR%2B4i%2FSv8b%5Co6Kq%2FwlEoj1vlYT5xwWJXrd%2B4D'
              '%5CrGhYO8EVj4pKR3nN0Pm435h0%2FkOLN096sBBNikyH01jhyhPQh8cdQVl2WqijwISSf'
              '%2BljB9jsXx3JHADeKpoDw5y2svMmqNygxqBNOf9M2%3A1633361173356; '
              'YD00517437729195%3AWM_NI=MYo1LH1TaBo53Tz1S6tKqq5Va58GMx'
              '%2BdCJ0IJOhTx89rbN5fQqleSi8lYqgK7rIpzUCw28R93cNZKboG48p%2FWGItyYaKncZVZL2'
              '%2FjCNsmjnAdz25GCTYS5DpQKQloNVTVDg%3D; '
              'YD00517437729195%3AWM_NIKE'
              '=9ca17ae2e6ffcda170e2e6ee93d273a9e7a682b57b8bbc8ba7c14f839e9eaef465988985dabb7abaafb8a8aa2af0fea7c3b92a8f87a1d2cf44f38cafa3ee3ff18cb6d2d23eb895bf92b85ea3ebf8a8d074e9bc8dabb3438a91a8b5fb34fbaeaeafb86e93afa486d263fcb49792e641f5ae8791f95f81a9fed9d133f1bd82bbca6aad99fcd9f32595998795fc53a395a284d95e9a94fed0e9498eada38bed4ba8a6fed6c64998879dd6c77c93959f8dee46968c9aa5e637e2a3; captcha_session_v2="2|1:0|10:1633360934|18:captcha_session_v2|88:a01kajZkbkk3SXVQRmdaRDFxYWdJaEhZdGt4ZVJneHBsV0gydnlFRTgrczJNUlpUNGM3VWRpZEQ1RGVWU3lUTA==|271ec831efbe0f190c3fc975a69db2fec59936fb76b4590001012cfe450ccf77"; captcha_ticket_v2="2|1:0|10:1633360938|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfV0RRa3NKYS4xXzFFSjk5bGtFOGs0NlZKUHBZMm5pdC1ia3A5SGVsNG9ubWVEMVVlQTlZTU9ma3ZnTHJLWWxJZU5CdXBLMXdabEJuVHJXODRaNVkxRExuOFktOGtTYy11LnFoWWVBcEw4STJEaU4ubTBtQi5QaFNoR2poNHhlYVMyMEpzV1kxWlNoeUhiNmluaS1fU2xFUUpfWmxmbVo1T1N5REUyZlpSY0xDOEJlQ0U1ci1HcTB6dkRuelVRZjJpT3NRLUdCdEkta1hEMjlJNS5vSWlGMUZyNVNOdUJCa2FBS21fajRkODVKSW1hU01ZMndUNUFCV3JhV1JMTDYuTEpleWpGQTVFRWxJRGlTeEtLXzJ1TlpZRzBoVy55NndjT1pqOUZtbS1HSDBHTXdhRTd5NmFTZG1vVkdYV2JVVFNSeDZBRFVicUk1VGt3al84c3RHMTB0STZtNVZLYjVTTVh2ZHhLX3BSb1hhU1lUQ0U4MmktYWpKSkJzUGlxZ2lfSUd5THgxdjFjMEZ5ZGpDcTYwbnoyMUItaFhGX3E0Umkwa093Mmd0XzVuXzhOVXdzNHZOQm5RcWxWckwyc0g2VGdnWml2a0dsWXZaYmQ5UVdHQzJvUVJNQWg0X2RaTDRzNmRISW9icGZQVjU4YnNOb2lfRWJ5Y0E1VjhxMyJ9|6c6d19639cbe9a5b64dcf08198b946258355357969570258484848b1d939b03e"; z_c0="2|1:0|10:1633360938|4:z_c0|92:Mi4xWG5LcUF3QUFBQUFBWUpoTVFzYXFFaVlBQUFCZ0FsVk5LbXBJWWdENjVIY1NHX1laSXR4M3ltR1pkNjNFMHlncnZ3|8c4641d6a42c781813786c63934e60b8b4f12d118810f349662d07808748b11c"; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1633361129; SESSIONID=SjTvSykf2NQ2kx9XZ2xm827QAgBpFIhg3etenQQmMLB; JOID=Vl8QBUhDLnr_jYS0IkH6rPDPQBoxE0YtjNn-3Ud2YynO4_uOeKozJ5yJhbUkgSnx8r6VmyqucC0MPy1c5h3kG-0=; osd=U1wSC0lGLXjxjIG3IE_7qfPNThs0EEQjjdz930l3ZirM7fqLe6g9JpmKh7slhCrz_L-QmCigcSgPPSNd4x7mFew=; KLBRSID=cdfcc1d45d024a211bb7144f66bda2cf|1633361132|1633359328 '
}


def comment(url):
    child_resp = requests.get(url, headers=headers)
    child_tree = etree.HTML(child_resp.text)
    comment_list = child_tree.xpath(
        "/html/body/div[1]/div/main/div/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div")
    for con in comment_list:
        name = con.xpath('./div/div/div[1]/div[1]/div/div/div[2]/div/div/text()')
        username = con.xpath('./div/div/div[1]/div[1]/div/div/div[1]/span//*/text()')
        data = con.xpath("./div/div/div[2]/div[1]/span/p/text()")
        print("name:", name, "username:", username,"data:", data)
    return


session = requests.session()
url = "https://www.zhihu.com/hot"
resp = session.get(url=url, headers=headers)
tree = etree.HTML(resp.text)
content_list = tree.xpath("/html/body/div[1]/div/main/div/div[3]/div[1]/div/div[2]/div/div/div[2]/section")
for content in content_list:
    href = content.xpath("./div[2]/a/@href")
    title = content.xpath("./div[2]/a/@title")
    hot = content.xpath("./div[2]/div/text()")
    print("href:", href, "title:", title, "hot:", hot)
    comment(href[0])
    # break
