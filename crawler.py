import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def news_crawler():
    url = "https://forum.gamer.com.tw/B.php?bsn=27487"
    ua = UserAgent().edge
    re   = requests.get(url, headers={'User-Agent': ua})

    content = ""

    soup = BeautifulSoup(re.text, "html.parser")
    data = soup.find_all("div", {"class": "b-list__tile"})
    
    for index, d in enumerate(data):
        if index <3:
            if (d.p != None):
                title = d.p.text
                content += "{}\n".format(title)
        else:
            break
    return content

print(news_crawler())