from flask import Flask, request, abort,render_template
import os,sys,sqlite3,json
from dotenv import load_dotenv
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,ImageSendMessage,StickerSendMessage,PostbackEvent,
    TemplateSendMessage,ButtonsTemplate,MessageTemplateAction,FlexSendMessage
)
from models.plot import return_message,picture
from models.judge import judge,return_pass_subject
import pandas as pd
app = Flask(__name__)

#Enviroment Setting
load_dotenv()
channel_secret=os.getenv('LINE_CHANNEL_SECRET')
channel_access_token=os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

#讀取成績單及通過標準
data=pd.read_csv('測試成績單.csv')
standar={'記憶':80,'理解':70,'應用':60,'分析':60,'評鑑':60,'創意':60}

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

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    try :
        reply_arr=[]                           #回覆的訊息list
        input_data=event.message.text.lower()  #大小寫都可搜尋
        content=return_message(data,input_data) #回覆成績資料
        grade_picture=picture(data,input_data)  #生成圖表及回傳URL
        pass_subject=judge(standar,data,input_data)  #產生通過的科目List
        content2=return_pass_subject(pass_subject)
        reply_arr.append(TextSendMessage(content))  #將文字訊系放入reply陣列
        reply_arr.append(ImageSendMessage(grade_picture,grade_picture)) #將圖表url放入回傳陣列
        if pass_subject :
            reply_arr.append(TextSendMessage(content2))
            reply_arr.append(StickerSendMessage(
                package_id='11537',
                sticker_id='52002735')
                )
            line_bot_api.reply_message(
                event.reply_token,reply_arr)
    except :
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage("查無此學號")
        )

@handler.add(PostbackEvent)
def handle_postback(event):
    if event.postback.data == '查詢成績' :
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage("請輸入您的學號")
        )
    elif event.postback.data == '課程簡報' :
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage("https://drive.google.com/drive/folders/1nP_q78_ZGVspPW3FgKP4Uy1HZIz7Exjk?usp=sharing")
        )
    elif event.postback.data == '補充教材' :
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage("https://drive.google.com/drive/folders/15yB50RwCJ-Qu8iz5PjpxrsDQmBrZyoin?usp=sharing")
        )
    elif event.postback.data == '課程規定' :
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage("https://drive.google.com/drive/folders/1fOI8PBk8spp1D_d3CNtruz-c3XsNuXlV?usp=sharing")
        )
    elif event.postback.data == '常見QA' :
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage("https://drive.google.com/drive/folders/1P6ulxiTASSq-h7VvwuisO-CPizDr_0za?usp=sharing")
        )


 

if __name__ == "__main__":  
    app.run(port=1234)