#发送post请求，数据必须要在字典中，通过data参数进行传递

import requests

url = "https://httpbin.org/post"

s=input("请输入您要翻译的英文单词:")
dat={"kw":s}
headers={"User-Agent":"Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.336(KHTML,like Gecko)Chrome/120.0.0.0 Safari/537.36"}
resp=  requests.post(url,data=dat,headers=headers)

print(resp.text)
print(resp.status_code)
#print(resp.json())

resp.close()