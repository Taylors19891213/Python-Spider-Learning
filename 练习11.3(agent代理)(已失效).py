import requests

proxies = {
    "https":"https://123.182.58.236:8089"
}
resp = requests.get("https://www.baidu.com",proxies=proxies)

print(resp.text)