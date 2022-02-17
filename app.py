from flask import Flask, request, abort, render_template
import matplotlib.pyplot as plt
import os, sys, sqlite3, json
from dotenv import load_dotenv
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,ImageSendMessage,StickerSendMessage,PostbackEvent)
from models.plot import flex_choose, flex_simple, picture,judge,return_pass_subject,create_data,search_ID_DICT,flex_grade
import pandas as pd
import re
from google.oauth2.service_account import Credentials
import gspread

import time


app = Flask(__name__)

#Enviroment Setting
load_dotenv()
channel_secret = os.getenv('LINE_CHANNEL_SECRET')
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

plt.switch_backend('agg') #不需要圖形介面的的backend
plt.rcParams['font.sans-serif'] = ['TaipeiSansTCBeta-Regular'] #顯示中文字

#讀取成績單及通過標準
data = create_data()
#print(data['ID'])   #test by QQ
#print(data)
standar = {'知識_40%':100,'能力_40%':70,'態度_20%':60}



#讀取google sheets
scope = ['https://www.googleapis.com/auth/spreadsheets'] #移出來讀一次就好，太耗效能 (成績有更動請重新啟動linebot)
creds = Credentials.from_service_account_file("linear-outcome-339410-10f813b7e005.json", scopes=scope)
sheet = gspread.authorize(creds).open_by_url('https://docs.google.com/spreadsheets/d/16EYLZIy5aOsCNXav9I3Oc-Av67R6lDK0uDfowvV4HNQ/edit#gid=0')

worksheet = sheet.get_worksheet(0)  
data = pd.DataFrame(worksheet.get_all_values())
data_filter = data.iloc[4:,:]

worksheet1 = sheet.get_worksheet(1)  
data1 = pd.DataFrame(worksheet1.get_all_values())
data_filter1 = data1.iloc[4:,:]

worksheet2 = sheet.get_worksheet(2)  
data2 = pd.DataFrame(worksheet2.get_all_values())
data_filter2 = data2.iloc[4:,:]

worksheet3 = sheet.get_worksheet(3)  
data3 = pd.DataFrame(worksheet3.get_all_values())
data_filter3 = data3.iloc[4:,:]

worksheet4 = sheet.get_worksheet(4)  
data4 = pd.DataFrame(worksheet4.get_all_values()) 
data_filter4 = data4.iloc[4:,:]

filtered_data = pd.concat([data_filter, data_filter1, data_filter2, data_filter3, data_filter4]).fillna(0)
filtered_data = filtered_data.replace('',0)
print('looooooooooooooook!!!!!!!!!!!\n'+str(filtered_data)+'\n')

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

    start = time.time() #計算運行時間
    
    input_data = event.message.text.upper()

    try :
        '''
        worksheet = sheet.get_worksheet(0)  
        data = pd.DataFrame(worksheet.get_all_values())
        data_filter = data.iloc[4:,:]
        '''
        #這裡移出來讀一次就好
        
        
        #row=data_filter.loc[data_filter.iloc[:,2]==input_data]
        row = filtered_data.loc[filtered_data.iloc[:,2] == input_data]
        #print(row)
        data_dict = row.to_dict('list')
        #print(data_dict)
        if len(data_dict[2]) != 0 :
            name = row.iloc[0,3]
            stu_id = row.iloc[0,2]
            print(name)
            knowledge_subtotal = row.iloc[0,20]
            CoreValues_subtotal = row.iloc[0,29]
            attitude_subtotal = row.iloc[0,33]
            picture(standar, filtered_data, stu_id)
            print(filtered_data)
            #total=row.iloc[0].iat[34]
            #line_bot_api.reply_message(event.reply_token,TextSendMessage(str(name) +'您好，知識應用：' + str(knowledge_subtotal) + '分，核心能力：' + str(CoreValues_subtotal) + '分，學習態度：' + str(attitude_subtotal) + '分，總分：' + str(total)))
        
            values = [float(knowledge_subtotal), float(CoreValues_subtotal), float(attitude_subtotal)]

            user_id = event.source.user_id
            print("user_id =", user_id)

            url = 'https://0cb4-61-56-180-227.ngrok.io//static//'+ str(stu_id) +'.png'
            print(url)
            
            #reply_arr.append(flex_grade(url, values))
            report_card = flex_grade(url, values)           
            line_bot_api.reply_message(event.reply_token, report_card)
            #line_bot_api.reply_message(event.reply_token, TextSendMessage('Hello'))
        
        
        '''
        if len(search_ID_DICT(data,input_data)['ID']) != 0 :  #判斷該學號是否存在
            grade_picture=picture(standar,data,input_data)     #生成圖表及回傳URL
            pass_subject=judge(standar,data,input_data)         #產生通過的科目List
            reply_arr.append(flex_grade(data,input_data,grade_picture))  #回覆成績資料
            if pass_subject :
                content=return_pass_subject(pass_subject)
                reply_arr.append(TextSendMessage(content))
                reply_arr.append(StickerSendMessage(
                    package_ids='11537',
                    sticker_id='52002735')
                )
            line_bot_api.reply_message(
                event.reply_token,reply_arr)
        '''
        print("The time used to execute this is given below")

        end = time.time()

        print(end - start)

        #if re.search('作業',input_data) :
        #    line_bot_api.reply_message(event.reply_token,TextSendMessage('https://euni.niu.edu.tw/'))
        if re.search('查詢成績',input_data):
            event.reply_token,TextSendMessage("請輸入您的學號")
        if re.search('作業繳交',input_data):
            choose_bubble = flex_choose()
            line_bot_api.reply_message(event.reply_token, choose_bubble)
        else :
            line_bot_api.reply_message(
            event.reply_token,TextSendMessage("查無此學號，請重新輸入。")
        )
    except :
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage("LineBot怪怪的，請聯絡老師或助教")
        )

@handler.add(PostbackEvent)
def handle_postback(event):
    if event.postback.data == '查詢成績' :
        line_bot_api.reply_message(           
            event.reply_token,TextSendMessage("請輸入您的學號")
        )
    elif event.postback.data == '作業繳交' :
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage("https://euni.niu.edu.tw/")
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
    app.run(port=8000)