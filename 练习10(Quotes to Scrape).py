# import requests
# from lxml import etree
# i = 1
# while i<=3:
#     url = f"https://quotes.toscrape.com/page/{i}/"
#     resp = requests.get(url)
#     html = etree.HTML(resp.text)
#     divs = html.xpath("/html/body/div/div[2]/div[1]/div")
#     i += 1
#     for div in divs:
#         quote = div.xpath("./span[1]/text()")[0]
#         author = div.xpath("./span[2]/small/text()")[0]
#         author_intro = div.xpath("./span[2]/a/@href")[0]
#         tags = div.xpath("./div/meta/@content")[0]
#         print("\nQuote: " + quote)
#         print("By " + author)
#         print("-Author_intro：" + "https://quotes.toscrape.com" + author_intro)
#         print("Tags：" + tags)
#
# resp.close()

import requests
from lxml import etree
page = 1
while True:
    print(f"========== 正在爬取第 {page} 页 ==========")
    url = f"https://quotes.toscrape.com/page/{page}/"
    resp = requests.get(url)
    html = etree.HTML(resp.text)

    # 1. 直接用 class 属性定位大盒子（告别绝对路径）
    divs = html.xpath('//div[@class="quote"]')

    # 如果这一页没有拿到任何名言，说明可能翻到最后一页之后了，跳出循环
    if not divs:
        break

    for div in divs:
        # 2. 同样用 class 属性精准提取，不再依赖 span[1]、span[2] 这种顺序
        quote = div.xpath('.//span[@class="text"]/text()')[0]
        author = div.xpath('.//small[@class="author"]/text()')[0]
        author_intro = div.xpath('.//span/a/@href')[0]

        # 3. 用常规方式提取标签列表
        tags = div.xpath('.//a[@class="tag"]/text()')

        print(f"Quote: {quote}")
        print(f"By {author}")
        print(f"-Author_intro: https://quotes.toscrape.com{author_intro}")
        print(f"Tags: {', '.join(tags)}")  # 把列表用逗号拼成字符串打印
        print(" " * 60)

    # 4. 聪明的翻页：寻找有没有 "Next" 按钮。如果有，page+1；如果没有，结束循环。
    next_btn = html.xpath('//li[@class="next"]/a/@href')
    if next_btn:
        page += 1
    else:
        print("🎉 已经是最后一页了，爬取结束！")
        break