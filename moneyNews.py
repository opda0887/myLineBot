import requests
from bs4 import BeautifulSoup

def MoneyNews_crawler():

    url = "https://news.ltn.com.tw/list/breakingnews/business"

    response = requests.get(url)

    contents = ""

    soup = BeautifulSoup(response.text, "html.parser")
    data = soup.find_all("a", {"class": "tit"})

    for index, d in enumerate(data):
        if index < 5:
            title = d.get("title")
            link = d.get("href")
            if (title != None):
                contents += "{}\n{}\n".format(title, link)
        else:
            break
    return contents

# print(MoneyNews_crawler())