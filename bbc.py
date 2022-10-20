from asyncio.windows_events import NULL
import requests
from bs4 import BeautifulSoup


def Cnn_crawler():
    url = "https://www.bbc.com/news/world"
    baseurl = "https://www.bbc.com{}"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    data = soup.find_all(
        "h3", {"class": "gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text"})

    data2 = soup.find_all(
        "a", {"class": "gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor"})

    content = ""

    for index, d in enumerate(data):
        if (index < 5):
            if (d != NULL):
                title = f"{d.text}"
                href = baseurl.format(data2[index].get("href"))
                content += title + "\n" + href + "\n" + "\n"

    return content


# print(Cnn_crawler())
