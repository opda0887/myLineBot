import requests
import json
import time

def Music_crawler():
    url = "https://kma.kkbox.com/charts/api/v1/daily?category=297&lang=tc&limit=50&terr=tw&type=newrelease"

    response = requests.get(url)
    
    # 將歌曲資訊json檔轉換成Python的字典型態
    data = json.loads(response.text)

    songs = data["data"]["charts"]["newrelease"]

    content = ""
    content += "本日歌曲排行：\n\n"
    index = 0
    for song in songs:
        if (index < 5):
            artist_name = song["artist_name"]
            song_name = song["song_name"]
            song_url = song["song_url"]
            song_timestamp = int(song["release_date"])
            # 從timestamp轉為日期格式
            song_date = time.strftime(
                "%Y/%m/%d", time.localtime(song_timestamp))
            
            content += "第{}名\n歌手：{}\n曲名：{}\n發布日期：{}\n連結：{}\n\n".format(index+1 ,artist_name, song_name, song_date, song_url)
            index = index + 1
    return content

# print(Music_crawler())