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
from music import *

app = Flask(__name__)  
# Channel Access Token 
line_bot_api = LineBotApi('qnz4kuyCErzakxej9E1OTYrKrE2PKEGouSgMhSncmWrrz4iarnpd3DrRkkN/YUtMFCmiogxiEQifR2NMKWTi8Oy6tgyKJgf2/L6jPrV4o14kl9zDuBxNOZnBbguF636Sb9i5J81tEQF2hXZuMwQP4AdB04t89/1O/w1cDnyilFU=')  
# Channel Secret
handler = WebhookHandler('616c083acfb57650e6cc0c5d20b351aa')

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
    c = Music_crawler()
    message = event.message.text

    # reply_token 只能用一次，用完一次就丟
    if "時事" in message:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=a))
    elif "財經" in message:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=b))
    elif "音樂" in message:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=c))
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message))

# main
#主程式 
import os 
if __name__ == "__main__":    
    port = int(os.environ.get('PORT', 5000))     
    app.run(host='0.0.0.0', port=port)