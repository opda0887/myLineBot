import requests
from bs4 import BeautifulSoup


def news_crawler():
    url = "https://news.google.com/topstories?hl=zh-TW&gl=TW&ceid=TW:zh-Hant"
    base = "https://news.google.com/articles/"
    re   = requests.get(url)

    content = ""

    soup = BeautifulSoup(re.text, "html.parser")
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

print(news_crawler())