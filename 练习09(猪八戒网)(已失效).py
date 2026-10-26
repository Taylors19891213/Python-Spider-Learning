from lxml import etree
import requests
url = requests.get("https://www.zbj.com/fw/?k=saas")
print(url.text)
html = etree.HTML(url.text)     #处理字符串

divs = html.xpath("/html/body/div[2]/div/div/div[3]/div/div[4]/div/div[2]/div/div[2]/div/text()")
print(divs)