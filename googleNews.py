import requests
from bs4 import BeautifulSoup


def GoogleNews_crawler():
    url = "https://news.google.com/topstories?hl=zh-TW&gl=TW&ceid=TW:zh-Hant"
    base = "https://news.google.com/articles/"
    response = requests.get(url)

    content = ""

    # 解析網頁原始碼
    soup = BeautifulSoup(response.text, "html.parser")
    # 找到標題資料
    data = soup.find_all("a", {"class": "DY5T1d RZIKme"})
    
    for index, d in enumerate(data):
        if index <5:
            if (d != None):
                title = d.text
                temp = d.get("href")
                href = base + temp[11:]
                content += "{}\n{}\n".format(title, href)
        else:
            break
    return content

print(GoogleNews_crawler())