from flask import Flask, request, abort,render_template
import os,sys,sqlite3
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,ImageSendMessage,StickerSendMessage
)
from models.plot import return_message,picture
import pandas as pd
app = Flask(__name__)

#Enviroment Setting
channel_secret=os.getenv('LINE_CHANNEL_SECRET')
channel_access_token=os.getenv('LINE_CHANNEL_ACCESS_TOKEN')

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

@app.route('/')
def home():
    return 'hello world'



@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    #app.logger.info("Request body: " + body) 會報錯先註解掉

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

#讀取成績單
data=pd.read_csv('測試成績單.csv')

#透過學號搜尋成績
# def search_ID_DICT(ID):
#     a=data.loc[data['ID']==ID]
#     data_dict=a.to_dict('list')
#     return data_dict

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    reply_arr=[]
    input_data=event.message.text.lower()  #大小寫都可搜尋
            
    content=return_message(data,input_data) #回覆成績資料
    grade_picture=picture(data,input_data)  #生成圖表及回傳URL
    reply_arr.append(TextSendMessage(content))  #將文字訊系放入reply陣列
    reply_arr.append(ImageSendMessage(grade_picture,grade_picture)) #將圖表url放入回傳陣列
    reply_arr.append(StickerSendMessage(
            package_id='11537',
            sticker_id='52002735')
    )
    line_bot_api.reply_message(
        event.reply_token,reply_arr)




if __name__ == "__main__":
    
    app.run(port=1234)