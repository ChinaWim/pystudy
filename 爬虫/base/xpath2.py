from lxml import etree

f = open("../res/html.html", mode="r")
html = f.read()
f.close()
tree = etree.HTML(html)
# 获取第一个,xpath索引是从第一个开始的
# result = tree.xpath("/html/body/ul/li[1]/a/text()")
# [@xxx=xxx] 属性筛选
# result = tree.xpath("/html/body/ol/li/a[@href='JAVA']/text()")

ol_li_list = tree.xpath("/html/body/ol/li")

# .是相对地址 @xxx获取属性值 text()获取文本值
for li in ol_li_list:
    result1 = li.xpath("./a/text()")
    print(result1)
    result2 = li.xpath("./a/@href")
    print(result2)

#浏览器，审查元素可以直接copy为xpath
