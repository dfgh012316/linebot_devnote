from flask import Flask, request, abort, render_template
import matplotlib.pyplot as plt
import os, sys, sqlite3, json, query_string
from dotenv import load_dotenv
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,ImageSendMessage,StickerSendMessage,PostbackEvent)
from models.plot import flex_rule, flex_addition, flex_ppt, flex_account, flex_choose, flex_homework, picture, judge, return_pass_subject, create_data, search_ID_DICT, flex_grade, test, true_or_false
from models.load_sheet import load_sheet
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
ngrok_url = os.getenv('NGROK_URL')

print(ngrok_url)
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

plt.switch_backend('agg') #不需要圖形介面的的backend
plt.rcParams['font.sans-serif'] = ['TaipeiSansTCBeta-Regular'] #顯示中文字

#讀取成績單及通過標準
standar = {'知識_40%':100,'能力_40%':70,'態度_20%':60}

filtered_data = load_sheet()

#建立SQLite資料庫
conn = sqlite3.connect('studentID_userID.db', check_same_thread=False)
cursor = conn.cursor()
#cursor.execute('CREATE TABLE StudentID_UserID(StudentID, UserID)')  #建立資料表
#conn.commit()

#機器人
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    
    # get request body as text
    body = request.get_data(as_text=True)
    print(body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'



@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):   
    input_data = event.message.text.upper()

    try :              
        row = filtered_data.loc[filtered_data.iloc[:,2] == input_data]       
        data_dict = row.to_dict('list')
        not_empty = (len(data_dict[2]) != 0)
        
        if not_empty :
            user_id = event.source.user_id         
            name = row.iloc[0,3]
            stu_id = row.iloc[0,2]
            reply_arr = [] # 用陣列可同時傳出多個訊息
            cursor.execute('select * from StudentID_UserID where UserID = ?', [user_id]) #執行SQL語法 (判斷UserID是否存在)
            conn.commit()
            result = cursor.fetchone() #紀錄是否存在 用這個判斷
            if(result == None):                
                account_bubble = flex_account(stu_id, user_id)
                line_bot_api.reply_message(event.reply_token, account_bubble)
            else:               
                cursor.execute('select * from StudentID_UserID where StudentID = ? AND UserID = ?', [stu_id, user_id]) #執行SQL語法 (判斷輸入學號是否match UserID)
                conn.commit()
                result = cursor.fetchone() #紀錄是否存在 用這個判斷
                
                if(result == None):
                    line_bot_api.reply_message(event.reply_token, TextSendMessage('您輸入的學號已被其他帳號綁定，有任何疑問請詢問助教或老師!'))
                else:
                    knowledge_subtotal = row.iloc[0,-3]
                    CoreValues_subtotal = row.iloc[0,-2]
                    attitude_subtotal = row.iloc[0,-1]
                    picture(standar, filtered_data, stu_id) #產生圖表
                    values = [float(knowledge_subtotal), float(CoreValues_subtotal), float(attitude_subtotal)]
                    url = ngrok_url + '//static//' + str(stu_id) +'.png'
                    report_card = flex_grade(url, values)
                    reply_arr.append(report_card)           
                    line_bot_api.reply_message(event.reply_token, reply_arr)
        # else:
        #     line_bot_api.reply_message(event.reply_token,TextSendMessage("查無此學號，請重新輸入。"))

        if re.search('作業繳交',input_data):
            choose_bubble = flex_homework()
            line_bot_api.reply_message(event.reply_token, choose_bubble)
        if re.search('測試',input_data):
            choose_bubble = test()
            line_bot_api.reply_message(event.reply_token, choose_bubble)
    except:
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage("LineBot怪怪的，請聯絡老師或助教")
        )

@handler.add(PostbackEvent)
def handle_postback(event):
    edata = query_string.parse(event.postback.data)
    if event.postback.data == '課程簡報' :
        choose_bubble = flex_ppt()
        line_bot_api.reply_message(event.reply_token, choose_bubble)
    elif event.postback.data == '查詢成績' :
        cursor.execute('select * from StudentID_UserID where UserID = ?', [event.source.user_id]) #執行SQL語法 (判斷輸入學號是否match UserID)
        conn.commit()       
        stu_id = cursor.fetchone()
        if(stu_id == None):
            line_bot_api.reply_message(
                event.reply_token,TextSendMessage("您的Line尚未與學號進行綁定，請輸入學號進行綁定！")
            )   
        else:
            stu_id = stu_id[0]
            action_bubble = true_or_false(stu_id)
            line_bot_api.reply_message(event.reply_token, action_bubble)
        # line_bot_api.reply_message(           
        #     event.reply_token,TextSendMessage(result[0]) #result[0] = 學號
        # )
    elif event.postback.data == '課程規定' :
        action_bubble = flex_rule()
        line_bot_api.reply_message(event.reply_token,action_bubble)
    elif event.postback.data == '補充教材' :
        action_bubble = flex_addition()
        line_bot_api.reply_message(event.reply_token,action_bubble)
    elif event.postback.data == '常見QA' :
        print('')
    else:
        if edata['answer'] == 'yes' :        
            cursor.execute('INSERT INTO StudentID_UserID VALUES (?, ?)', (edata['stu_id'], edata['user_id'])) #將UserID和學號做綁定 並記錄在SQLite內
            conn.commit()
            sqlite3.SQLITE_UPDATE
            line_bot_api.reply_message(event.reply_token, TextSendMessage('進行綁定中... 綁定完成!'))
        elif edata['answer'] == 'no' :
            line_bot_api.reply_message(event.reply_token, TextSendMessage('取消綁定，請重新操作。'))
        else:
            line_bot_api.reply_message(event.reply_token, TextSendMessage('請重新操作。'))   
    # elif edata['action'] == '心理學a':
    #     action_bubble = flex_PSY_A()
    #     line_bot_api.reply_message(event.reply_token, action_bubble)
    # elif edata['action'] == '心理學b':
    #     action_bubble = flex_PSY_B()
    #     line_bot_api.reply_message(event.reply_token, action_bubble)
    # elif edata['action'] == '心理健康a':
    #     action_bubble = flex_MHD_A()
    #     line_bot_api.reply_message(event.reply_token, action_bubble)
    # elif edata['action'] == '心理健康b':
    #     action_bubble = flex_MHD_B()
    #     line_bot_api.reply_message(event.reply_token, action_bubble)
    # elif edata['action'] == '職場/蘭陽采風':
    #     action_bubble = flex_IRW()
    #     line_bot_api.reply_message(event.reply_token, action_bubble)
    # elif edata['action'] == '社會脈動':
    #     action_bubble = flex_Social()
    #     line_bot_api.reply_message(event.reply_token, action_bubble)    
    # elif edata['action'] == '課程簡報' :
    #     action_bubble = flex_PPT()
    #     line_bot_api.reply_message(event.reply_token, action_bubble)
    # elif edata['action'] == '補充教材' :
    #     action_bubble = flex_Addition()
    #     line_bot_api.reply_message(event.reply_token, action_bubble)

if __name__ == "__main__":  
    app.run(port=80)