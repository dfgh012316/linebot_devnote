# LineBot開發


# Demo

![BotQR.png](BotQR.png)

1.請掃描QR Code加入好友

2.Demo用學號：b0742024  

3.輸入後可以查看目前成績、自評成績、是否通過老師設定門檻

# 使用技術與考量

1. LineBot (Python+Flask)  服務內容較為簡單 輕量級框架較為適合
2. Models(matplotlib+pandas+numpy) 讀取成績內容進行操作並繪製圖表
3. Database(excel) 方便TA直接輸入成績 無須再將成績csv檔輸入資料庫

# 參考資料

[line/line-bot-sdk-python](https://github.com/line/line-bot-sdk-python)

[Flask + Apache 架在windows上](https://medium.com/@ddoo8059/flask-apache-%E6%9E%B6%E5%9C%A8windows%E4%B8%8A-a47386ec913b)

[[Pandas教學]5個實用的Pandas讀取Excel檔案資料技巧](https://www.learncodewithmike.com/2020/12/read-excel-file-using-pandas.html?fbclid=IwAR0B71QJu4tUU-kLQOB0zylUxtM4mCKb9lWXLtTJS_sHTMEPntYMiDjgbRs)

[Sending Flex Messages](https://developers.line.biz/en/docs/messaging-api/using-flex-messages/#sending-hello-world)

# 遭遇問題

1. 在虛擬環境中，matplotlib的中文亂碼問題。
需要去 anaconda中的env 安裝matplotlib字體的資料夾增加字體可參考下方教學連結

    [Python教學-如何解決matplotlib中文亂碼問題](https://pyecontech.com/2020/03/27/python%E6%95%99%E5%AD%B8-%E5%A6%82%E4%BD%95%E8%A7%A3%E6%B1%BAmatplotlib%E4%B8%AD%E6%96%87%E4%BA%82%E7%A2%BC%E5%95%8F%E9%A1%8C/)

2. Linebot如何傳遞複數訊息給使用者?

    ```python
    reply_arr=[]
    reply_arr.append(TextSendMessage("Demo")
    reply_arr.append(TextSendMessage("Test")
    line_bot_api.reply_message(event.reply_token,reply_arr)
    ```

3. plt.savefig()多次使用會覆蓋前面的圖片，須加上plt.close()
4. Git如何返回前一個版本以及刪除某次commit

    ```bash
    !git reset --hard HEAD~  #等於~1  ~n等於回到前幾個版本
    ```

5. df中空值要補0 否則無法畫圖

    ```python
    df=df.fillna(0)
    ```

6. 如何在成績達標後變色？將通過的科目存成一個[(math,0),(english,1)]這樣的list 後如下方式處理

    ```python
    rects1 = ax.bar(x +width/2, grade, width,color='#84C1FF')   #學生目前成績
    for i, bar in enumerate(rects1): 
                if flag[i] == 0 : 
                    bar.set_color("#FF7575")      #不及格的顏色
    ```

7. 如何讀取一份excel中的多個sheet?將不同的sheet合併到一個DataFrame中

    ```python
    def create_data():
        df = pd.DataFrame()
        data = pd.read_excel("測試成績單.xlsx", sheet_name=None,engine='openpyxl')
        sheet = pd.ExcelFile("測試成績單.xlsx",engine='openpyxl')
        for s_name in sheet.sheet_names:
            df = pd.concat([df, data.get(s_name)], ignore_index=False)

        return df
    ```

# Future Work

- [x]  將成績訊息改用flex message傳送
- [ ]  部署至apache 伺服器而非使用ngrok
- [ ]  美化Flex Message 的排版
- [ ]  將目前code寫成物件導向
- [ ]  增加程式碼彈性與使用性，方便老師新增科目、調整評分、修改圖表顏色等
