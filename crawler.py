import requests
from bs4 import BeautifulSoup


def news_crawler():
    url = "https://news.google.com"
    re   = requests.get(url)

    content = ""

    soup = BeautifulSoup(re.text, "html.parser")
    data = soup.find_all("a", {"class": "DY5T1d RZIKme"})
    
    for index, d in enumerate(data):
        if index <8:
            if (d != None):
                title = d.text
                content += "{}\n".format(title)
        else:
            break
    return content