import requests
#会话
session = requests.session()
data = {
"username":"ffff",
"password":"1111"
}
url = "https://quotes.toscrape.com/login"
session.post(url,data=data)
resp = session.get("https://quotes.toscrape.com/tag/inspirational/")
print(resp.text)