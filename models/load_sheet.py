# 讀取google sheets
from dotenv import load_dotenv
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import os

def load_sheet():
    load_dotenv()
    scope = ['https://www.googleapis.com/auth/spreadsheets'] # 移出來讀一次就好，太耗效能 (成績有更動請重新啟動linebot)
    creds = Credentials.from_service_account_file("linear-outcome-339410-10f813b7e005.json", scopes=scope)
    sheet = gspread.authorize(creds).open_by_url(os.getenv('GOOGLE_SHEET_URL'))

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
    filtered_data = filtered_data.replace('#DIV/0!',0)

    return filtered_data