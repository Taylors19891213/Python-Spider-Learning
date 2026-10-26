# #拿到页面源代码 requests
# #通过re来提取想要的有用信息 re

import requests
import re
import csv
#拿到数据
url="https://movie.douban.com/top250"
headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36 Edg/155.0.0.0"}
resp = requests.get(url,headers=headers)
page_content=resp.text
print(page_content)

#解析数据
obj = re.compile(r"""<li>.*?<div class="item">
.*?<span class="title">(?P<name>.*?)</span>
.*?<p class="">.*?<br>(?P<year>.*?)&nbsp
.*?<span class="rating_num" property="v:average">(?P<rating>.*?)</span>.*?<span>(?P<audience>.*?)
人评价</span>""",re.S)
#开始匹配
namelist=obj.finditer(page_content)
f = open("data.csv","w",encoding="utf-8")
csvwriter = csv.writer(f)
for i in namelist:
    print(i.group("name"))
    print(i.group("year"))
    print(i.group("rating"))
    print(i.group("audience"))
    dic = i.groupdict()
    dic['year']=dic['year'].strip()
    csvwriter.writerow(dic.values())

f.close()
print("done")



# # 极简版：只抓标题，看看能不能匹配到
# import re
# import requests
#
# url="https://movie.douban.com/top250"
# headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36 Edg/155.0.0.0"}
# resp = requests.get(url,headers=headers)
# page_content=resp.text
# obj = re.compile(r'<span class="title">(?P<name>.*?)</span>', re.S)
# namelist = obj.finditer(page_content)
#
# count = 0
# for i in namelist:
#     count += 1
#     print(i.group("name"))
#
# print(f"一共找到了 {count} 个电影名字")