# 第三种解析 xpath 使用最多，是在xml文档中搜索内容的一门语言
# html是xml的一个子集
# 安装lxml模块 pip install -i https://mirrors.aliyun.com/pypi/simple/ lxml

from lxml import etree

f = open("../res/xml.xml", mode="r")
xml = f.read()
f.close()

tree = etree.XML(xml)
# result = tree.xpath("/bookstore/book/title/text()") # text() 拿文本
# result = tree.xpath("/bookstore/book//text()")  # 两斜杠模糊匹配
result = tree.xpath("/bookstore/book/*/text()")  # * 任意节点，通配符
print(result)
