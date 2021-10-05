# .* 贪婪匹配
# .*? 惰性匹配
import re
# findall
lst = re.findall(r"\d+", "我的电话号是：10086，我女朋友的电话是：10010")
print(lst)
# finditer
it = re.finditer(r"\d+", "我的电话号是：10086，我女朋友的电话是：10010")
for i in it:
    print(i.group())

# search 找到一个结果就返回, 全文匹配
s = re.search(r"\d+", "我的电话号是：10086，我女朋友的电话是：10010")
print(s.group())

# math 从头开始匹配 默认在你正则加^
m = re.match(r"\d+", "10086，我女朋友的电话是：10010")
print(m.group())

# 预加载正则表达式
obj = re.compile(r"\d+")
print("--")
ret = obj.finditer("我的电话号是：10086，我女朋友的电话是：10010")
for i in ret:
    print(i.group())


# (?P<分组名字>正则) 可以单独从正则匹配的内容中进一步提取内容  obj.group("分组名字")
