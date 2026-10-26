import requests
from bs4 import BeautifulSoup
import csv

# 伪装浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

url = "http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml"
resp = requests.get(url, headers=headers)
resp.encoding = "utf-8"

f = open("菜价.csv", mode="w", encoding="utf-8", newline="")
csvwriter = csv.writer(f)

page = BeautifulSoup(resp.text, "html.parser")
table = page.find("table", attrs={"class": "hq_table"})
trs = table.fin_dall("tr")[1:]

for tr in trs:
    tds = tr.find_all("td")
    name = tds[0].text
    low = tds[1].text
    avg = tds[2].text
    high = tds[3].text
    gui = tds[4].text
    kind = tds[5].text
    date = tds[6].text
    csvwriter.writerow([name, low, avg, high, gui, kind, date])

f.close()
print("over!!!!")