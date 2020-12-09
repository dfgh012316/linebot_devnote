# LineBot開發

# 使用技術

1. LineBot (Python+Flask)
2. Models(matplotlib+pandas+numpy)
3. Deploy(ngrok or Heroku or Apache) +wsgi on windows

# 參考資料

[line/line-bot-sdk-python](https://github.com/line/line-bot-sdk-python)

[用 Flask 與 SQLite 架抽籤網站](https://blog.liang2.tw/posts/2015/09/flask-draw-member/)

[Flask + Apache 架在windows上](https://medium.com/@ddoo8059/flask-apache-%E6%9E%B6%E5%9C%A8windows%E4%B8%8A-a47386ec913b)

[[Pandas教學]5個實用的Pandas讀取Excel檔案資料技巧](https://www.learncodewithmike.com/2020/12/read-excel-file-using-pandas.html?fbclid=IwAR0B71QJu4tUU-kLQOB0zylUxtM4mCKb9lWXLtTJS_sHTMEPntYMiDjgbRs)

# 待處理問題

- [ ]  讀取一份csv檔中多個sheet
- [ ]  圖表達標後變色
- [ ]  顯示平均成績的圖表

# 遭遇問題

1. 在虛擬環境中，matplotlib的中文亂碼問題。
需要去 anaconda中的env 安裝matplotlib字體的資料夾增加字體
2. Android手機無法正常顯示linebot傳送的圖片
似乎是ngrok的問題，在ios及電腦版上皆正常
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
8. df中空值要補0  df.fillna(0) 否則無法畫圖

```python
!git reset --hard HEAD~  #等於~1  ~n等於回到前幾個版本
```

```python
int(df['國文'])  # invalid
df['國文'].astype(int)  #OK
```