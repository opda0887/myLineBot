from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re

app = Flask(__name__)  
# Channel Access Token 
line_bot_api = LineBotApi('qnz4kuyCErzakxej9E1OTYrKrE2PKEGouSgMhSncmWrrz4iarnpd3DrRkkN/YUtMFCmiogxiEQifR2NMKWTi8Oy6tgyKJgf2/L6jPrV4o14kl9zDuBxNOZnBbguF636Sb9i5J81tEQF2hXZuMwQP4AdB04t89/1O/w1cDnyilFU=')  
# Channel Secret
handler = WebhookHandler('616c083acfb57650e6cc0c5d20b351aa')

line_bot_api.push_message('U6ea49ab8c64a47cfa18fd9993d1ac351', TextSendMessage(text='Can Start~'))

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
            print(title.p.text)
            content += f"{title.p.text}\n"
    content += f"{url}"
    return content


# 監聽所有來自 /callback 的 Post Request 
@app.route("/callback", methods=['POST']) 
def callback():     
    # get X-Line-Signature header value     
    signature = request.headers['X-Line-Signature']
    # get request body as text     
    body = request.get_data(as_text=True)     
    app.logger.info("Request body: " + body)      
    # handle webhook body     
    try:         
        handler.handle(body, signature)     
    except InvalidSignatureError:         
        abort(400)      
    return 'OK'

# send text
@handler.add(MessageEvent, message=TextMessage) 
def handle_message(event):
    a = IBaha()
    message = event.message.text
    if re.match("搜尋", message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage(a))
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(message))

# main
#主程式 
import os 
if __name__ == "__main__":    
    port = int(os.environ.get('PORT', 5000))     
    app.run(host='0.0.0.0', port=port)