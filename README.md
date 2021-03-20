# LineBot開發

# Demo

![_2021-03-20_4.10.48.png](_2021-03-20_4.10.48.png)

1.請掃描二維碼加入好友

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

[python(flask) + mod_wsgi + apache windows下環境搭建](https://www.itread01.com/p/515653.html)

[Python CGI环境搭建XAMPP配置_Jechen-CSDN博客](https://blog.csdn.net/weixin_42116406/article/details/100536760)

# 遭遇問題

1. 在虛擬環境中，matplotlib的中文亂碼問題。
需要去 anaconda中的env 安裝matplotlib字體的資料夾增加字體
2. Android手機無法正常顯示linebot傳送的圖片
LINE更新最新版後此問題已解決
3. 將圖片透過Linebot傳送給使用者
似乎不能傳本地端的圖片?將圖片存在flask中的static資料夾
將 https://xxx.xxxxxx.io//static//xxxx.jpg當網址傳遞即可
4. linebot縮圖與實際圖片不符
將本來的jpg檔換存png檔洗掉之前的縮圖紀錄解決
5. Linebot如何傳遞複數訊息給使用者?
要使用list儲存要傳遞的訊息再將陣列傳遞出去
需要注意的是  並不是直接將要傳遞的內容放進list
而是要針對傳遞的訊息內容(如Textsendmessage 或 Imagesendmessage 放進該函式中再一起存入List 
6. plt.savefig()多次使用會覆蓋前面的圖片，須加上plt.close()
7. Git如何返回前一個版本以及刪除某次commit

    ```bash
    !git reset --hard HEAD~  #等於~1  ~n等於回到前幾個版本
    ```

8. df中空值要補0 否則無法畫圖

    ```python
    df=df.fillna(0)
    ```

9. 如何在成績達標後變色？將通過的科目存成一個[(math,0),(english,1)]這樣的list 後用bars去接本來的plt.bar()後用for迴圈去迭代bars符合條件時用set_color去變色
10. 如何讀取一份excel中的多個sheet?將不同的sheet合併到一個DataFrame中

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

- [ ]  增加程式碼彈性與使用性，方便老師新增科目、調整評分、修改圖表顏色等
- [ ]  部署至apache 伺服器而非使用ngrok