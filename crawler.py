# crawler
from urllib import request as req
from fake_useragent import UserAgent
import bs4

def IBaha():
    url = "https://forum.gamer.com.tw/B.php?bsn=27487"
    #建立 Request 物件，附加Headers的資訊，讓google伺服器以為我們是一般使用者
    ua = UserAgent().edge
    request=req.Request(url, headers={
        "User-Agent": ua
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    #解析原始碼，得到每篇標題
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div", class_="b-list__tile") #找全部 class="title"的div標籤  #把div裡面有內容的影印出來
    content = ""
    for title in titles:
        if (title.p != None):
            content += f"{title.p.text}\n"
    content += f"{url}"
    return content

