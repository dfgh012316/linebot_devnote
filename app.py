from flask import Flask, request, abort
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv
from linebot import (
    LineBotApi, WebhookHandler)
from linebot.exceptions import (
    InvalidSignatureError)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage)
from models.plot import (
  picture, judge, return_pass_subject, create_data, search_ID_DICT, flex_grade)

app = Flask(__name__)

# Enviroment Setting
load_dotenv()
channel_secret = os.getenv('LINE_CHANNEL_SECRET')
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)
plt.switch_backend('agg')
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']

# 讀取成績單及通過標準
data = create_data()
standar = {'知識_40%': 80, '能力_40%': 70, '態度_20%': 60}


# 機器人
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    # app.logger.info("Request body: " + body) 會報錯先註解掉

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. \
               Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    try:
        reply_arr = []
        input_data = event.message.text.upper()
        if len(search_ID_DICT(data, input_data)['ID']) != 0:
            grade_picture = picture(standar, data, input_data)
            pass_subject = judge(standar, data, input_data)
            reply_arr.append(flex_grade(data, input_data, grade_picture))
            if pass_subject:
                content = return_pass_subject(pass_subject)
                reply_arr.append(TextSendMessage(content))
                reply_arr.append(StickerSendMessage(
                    package_id='11537',
                    sticker_id='52002735'))
            line_bot_api.reply_message(event.reply_token, reply_arr)
        else:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage("查無此學號，請重新輸入。"))
    except input_data.error:
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage("LineBot怪怪的請聯絡老師或助教"))


if __name__ == "__main__":
    app.run(port=1234)
