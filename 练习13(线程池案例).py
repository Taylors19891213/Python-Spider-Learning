#1.如何提取单个页面的数据
#2.上线程池，多个页面同时抓取

import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
import csv

f=open("douban.data.csv",mode="w",encoding="utf-8")
csvwriter = csv.writer(f)

def download_one_page(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36 Edg/156.0.0.0"
    }
    resp = requests.get(url,headers=headers)
    resp.encoding="utf-8"
    html=etree.HTML(resp.text)
    li_list=html.xpath("//*[@id='content']/div/div[1]/ol/li")

    for li in li_list:
        info=li.xpath('./div/div[2]/div[1]/a/@href')[0]
        title=li.xpath('./div/div[2]/div[1]/a/span[1]/text()')[0]

        csvwriter.writerow([title,info])
        print([title,info])

if __name__ == '__main__':
    #for i in range(1,250):       #效率低下
    #    download_one_page("https://movie.douban.com/top250")
    with ThreadPoolExecutor(max_workers=50) as t:
        for i in range(0,250,25):
            t.submit(download_one_page,f"https://movie.douban.com/top250?start={i}&filter=")

    print("下载完毕！")