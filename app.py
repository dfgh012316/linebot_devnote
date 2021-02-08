# #!/usr/bin/python # 
# # -*- coding: UTF-8 -*-

# print('Content-type: text/html\n\n')



from flask import Flask, request, abort,render_template
import matplotlib.pyplot as plt
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
from models.plot import return_message,picture,judge,return_pass_subject,create_data,search_ID_DICT
import pandas as pd
app = Flask(__name__)

#Enviroment Setting
load_dotenv()
channel_secret=os.getenv('LINE_CHANNEL_SECRET')
channel_access_token=os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

plt.switch_backend('agg') #不需要圖形介面的的backend
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta'] #顯示中文字

#讀取成績單及通過標準
data=create_data()
standar={'知識_40%':80,'能力_40%':70,'態度_20%':60}

#機器人
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
        input_data=event.message.text.upper()  #大小寫都可搜尋
        if len(search_ID_DICT(data,input_data)['ID']) != 0 :  #判斷是否有該學號
            content=return_message(data,input_data) #回覆成績資料
            grade_picture=picture(standar,data,input_data)  #生成圖表及回傳URL
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
        else :
            line_bot_api.reply_message(
            event.reply_token,TextSendMessage("查無此學號，請重新輸入。")
        )

    except :
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage("LineBot怪怪的請聯絡老師或助教")
        )

@handler.add(PostbackEvent)
def handle_postback(event):
    if event.postback.data == '查詢成績' :
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage("請輸入您的學號+安全碼(兩碼)")
        )
    elif event.postback.data == '重要公告' :
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage("目前尚未有公告唷！")
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