import requests
url = "https://www.pearvideo.com/video_1807896"
contID = url.split("_")[1]
s_v_url= f"https://www.pearvideo.com/videoStatus.jsp?contId={contID}&mrd=0.7481687248986483"

headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36 Edg/156.0.0.0"
,"Referer":"https://www.pearvideo.com/video_1807896"
}
resp = requests.get(s_v_url,headers=headers)
dic = resp.json()

srcUrl = dic["videoInfo"]["videos"]["srcUrl"]
systemTime = dic["systemTime"]
srcUrl = srcUrl.replace(systemTime,f"cont-{contID}")
print(srcUrl)

with open("a.mp4","wb") as f:
    f.write(requests.get(srcUrl).content)





# https://video.pearvideo.com/mp4/short/20261019/1793014042214-16083516-hd.mp4
# https://video.pearvideo.com/mp4/short/20261019/cont-1807896-16083516-hd.mp4