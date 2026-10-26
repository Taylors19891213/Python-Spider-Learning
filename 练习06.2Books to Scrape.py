#find_all返回一个列表
import requests
import bs4

#提取网页源代码
url = "https://books.toscrape.com/catalogue/page-2.html"
resp = requests.get(url)
page = bs4.BeautifulSoup(resp.text, "html.parser")#保证能够被bs4读取

articles = page.find_all("article", class_="product_pod")

for article in articles:
    # 1. 提取书名（在 a 标签的 title 属性里）
    name = article.find("h3").find("a")["title"]

    # 2. 提取图片链接（在 img 标签的 src 属性里）
    # 注意：这个网站的图片是相对路径，需要拼接基础 URL
    img_tag = article.find("img")
    img_rel_url = img_tag["src"]
    img_full_url = "https://books.toscrape.com/" + img_rel_url.replace("../", "")

    print(f"书名: {name}")
    print(f"图片链接: {img_full_url}")
    print("-" * 30)