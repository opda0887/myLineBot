import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def news_crawler():
    url = "https://forum.gamer.com.tw/B.php?bsn=60076"
    ua = UserAgent().edge
    re   = requests.get(url, headers={'User-Agent': ua})

    content = ""

    soup = BeautifulSoup(re.text, "html.parser")
    data = soup.find_all("p", {"class": "b-list__main__title"})
    
    for index, d in enumerate(data):
        if index <20:
            if (d != None):
                title = d.text
                content += "{}\n".format(title)
        else:
            break
    return content

print(news_crawler())