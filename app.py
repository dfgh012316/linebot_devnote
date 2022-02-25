from flask import Flask, request, abort, render_template
import matplotlib.pyplot as plt
import os, sys, sqlite3, json, query_string
from dotenv import load_dotenv
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,ImageSendMessage,StickerSendMessage,PostbackEvent)
from models.plot import flex_account, flex_choose, flex_simple, picture,judge,return_pass_subject,create_data,search_ID_DICT,flex_grade
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
#data = create_data()
#print(data['ID'])   #test by QQ
#print(data)
standar = {'知識_40%':100,'能力_40%':70,'態度_20%':60}



# 讀取google sheets
scope = ['https://www.googleapis.com/auth/spreadsheets'] # 移出來讀一次就好，太耗效能 (成績有更動請重新啟動linebot)
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
filtered_data = filtered_data.replace('',0) # 成績單上不是數值型態
print('looooooooooooooook!!!!!!!!!!!\n'+str(filtered_data)+'\n')



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
        #這裡移出來讀一次就好       
        
        row = filtered_data.loc[filtered_data.iloc[:,2] == input_data]       
        data_dict = row.to_dict('list')
        
        if len(data_dict[2]) != 0 :
            user_id = event.source.user_id
            print("user_id =", user_id)           
            name = row.iloc[0,3]
            stu_id = row.iloc[0,2]
            print(type(user_id))
            reply_arr = []
            
            cursor.execute('select * from StudentID_UserID where UserID = ?', [user_id]) #執行SQL語法 (判斷UserID是否存在)
            conn.commit()
            result = cursor.fetchone() #紀錄是否存在 用這個判斷
            print(result)

            if(result == None):                
                account_bubble = flex_account(stu_id, user_id)
                line_bot_api.reply_message(event.reply_token, account_bubble)
            else:
                reply_arr.append(TextSendMessage('學號已綁定!'))
                #line_bot_api.reply_message(event.reply_token, TextSendMessage('是否要將學號綁定至Line帳號?'))
            #if(re.search('否',input_data)):
                #line_bot_api.reply_message(event.reply_token, TextSendMessage('取消綁定，請重新輸入學號。'))
            #elif(re.search('是',input_data)):                   
                #reply_arr.append(TextSendMessage('進行綁定中... 綁定完成!'))
                #cursor.execute('INSERT INTO StudentID_UserID VALUES (?, ?)', (stu_id, user_id)) #將UserID和學號做綁定 並記錄在SQLite內
                #conn.commit()
                #sqlite3.SQLITE_UPDATE

                print(name)
                knowledge_subtotal = row.iloc[0,20]
                CoreValues_subtotal = row.iloc[0,29]
                attitude_subtotal = row.iloc[0,33]
                picture(standar, filtered_data, stu_id) #產生圖表
                print(filtered_data)
            
                values = [float(knowledge_subtotal), float(CoreValues_subtotal), float(attitude_subtotal)]

                url = 'https://5708-61-56-180-227.ngrok.io//static//'+ str(stu_id) +'.png'
                print(url)

                #reply_arr.append(flex_grade(url, values))
                report_card = flex_grade(url, values)
                reply_arr.append(report_card)           
                #line_bot_api.reply_message(event.reply_token, report_card)
                #line_bot_api.reply_message(event.reply_token, TextSendMessage('Hello'))
                line_bot_api.reply_message(event.reply_token, reply_arr)
        
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
        #if re.search('綁定帳號',input_data):
        #    account_bubble = flex_account()
        #    line_bot_api.reply_message(event.reply_token, account_bubble)
        #if re.search('確定綁定',input_data):
        #    reply_arr.append(TextSendMessage('進行綁定中... 綁定完成!'))
        #    cursor.execute('INSERT INTO StudentID_UserID VALUES (?, ?)', (stu_id, user_id)) #將UserID和學號做綁定 並記錄在SQLite內
        #    conn.commit()
        #    sqlite3.SQLITE_UPDATE
        else:
            line_bot_api.reply_message(
            event.reply_token,TextSendMessage("查無此學號，請重新輸入。")
        )
    except:
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage("LineBot怪怪的，請聯絡老師或助教")
        )

@handler.add(PostbackEvent)
def handle_postback(event):
    edata = query_string.parse(event.postback.data)
    print(event.postback.data)
    print(edata)
    if event.postback.data == '查詢成績' :
        line_bot_api.reply_message(           
            event.reply_token,TextSendMessage("請輸入您的學號")
        )
    elif edata['answer'] == 'yes' :        
        cursor.execute('INSERT INTO StudentID_UserID VALUES (?, ?)', (edata['stu_id'], edata['user_id'])) #將UserID和學號做綁定 並記錄在SQLite內
        conn.commit()
        sqlite3.SQLITE_UPDATE
        line_bot_api.reply_message(event.reply_token, TextSendMessage('進行綁定中... 綁定完成!'))
    elif edata['answer'] == 'no' :
        line_bot_api.reply_message(event.reply_token, TextSendMessage('取消綁定，請重新操作。'))
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