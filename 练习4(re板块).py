import re

# #findall:匹配字符串中所有符合正则的内容
# list = re.findall(r"\d+","我的电话号码是：15211127626")
# print(list)

# #finditer:匹配字符串中的所有的内容[返回的是迭代器]，从迭代器中拿到内容需要.group()
# list2 = re.finditer(r"\d+","我的电话号码是；15211127626，母亲的电话号码是：15390804490")
# for i in list2:
#     print(i.group())

# #research:找到一个结果就返回，返回match对象，拿数据需要.group()
# list3 = re.search(r"\d+","我的电话号码是；15211127626，母亲的电话号码是：15390804490")
# print(list3.group())
# print(list3)

# #match:从头开始匹配
# list4 = re.match(r"\d+","15211127626，母亲的电话号码是：15390804490")
# print(list4.group())

#预加载正则表达式  re.compile
obj = re.compile(r"\d+")
result = obj.findall("my QQ:2453802426 , my phone number:15211127626")
print(result)

#(?P<分组名字>正则) 可以单独从正则匹配的内容中进一步提取内容
#re.S : 让. 也能够匹配换行符
