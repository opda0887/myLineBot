from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from googleNews import *
from moneyNews import *

app = Flask(__name__)  
# Channel Access Token 
line_bot_api = LineBotApi('qnz4kuyCErzakxej9E1OTYrKrE2PKEGouSgMhSncmWrrz4iarnpd3DrRkkN/YUtMFCmiogxiEQifR2NMKWTi8Oy6tgyKJgf2/L6jPrV4o14kl9zDuBxNOZnBbguF636Sb9i5J81tEQF2hXZuMwQP4AdB04t89/1O/w1cDnyilFU=')  
# Channel Secret
handler = WebhookHandler('616c083acfb57650e6cc0c5d20b351aa')

text = "1. 輸入 時事 可查詢最近新聞\n2. 輸入 財經 可查詢最近財經資訊\n3. 除此之外為一般的聊天機器人"
line_bot_api.push_message('U6ea49ab8c64a47cfa18fd9993d1ac351', TextSendMessage(text=text))


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
    a = GoogleNews_crawler()
    b = MoneyNews_crawler()
    message = event.message.text
    if "時事" in message:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=a))
    elif "財經" in message:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=b))
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message))

# main
#主程式 
import os 
if __name__ == "__main__":    
    port = int(os.environ.get('PORT', 5000))     
    app.run(host='0.0.0.0', port=port)