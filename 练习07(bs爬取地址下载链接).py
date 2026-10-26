import requests
import bs4
import time
#得到页面源代码
url ="https://www.bizhihui.com/"
resp = requests.get(url)
resp.encoding ="usf-8"

main_page = bs4.BeautifulSoup(resp.text, "html.parser") #用b4解析页面源代码
list = main_page.find_all("div",class_="item-info2")   #提取所有div标签到列表中

for div_tag in list:
    a_tag = div_tag.find("a")       #提取div标签中的a标签
    if a_tag:                       #防止a标签无对应内容
        href = a_tag.get("href")    #得到a标签属性对应的值（子页面链接）
        #bs解析子页面源代码
        c_p_resp = requests.get(href)
        c_p_resp.encoding = "utf-8"
        c_p_text = c_p_resp.text
        c_p = bs4.BeautifulSoup(c_p_text, "html.parser")

        c_div_tag = c_p.find("div",class_="down-box-m")      #找到div标签
        c_a_tag = c_div_tag.find("a")                              #找到div中的a标签
        if c_a_tag:
            c_href = c_a_tag.get("href")                           #得到下载地址
            print("壁纸标签：" + a_tag.get("title"))
            print("下载地址：" + c_href)
            print("-----------------------------------------------------------------")
            time.sleep(1)
