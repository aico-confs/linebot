from flask import Flask, request, abort
# from flask.logging import create_logger
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)

from linebot.models import *
import urllib.request as r
import re

#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========

app = Flask(__name__)
# abcd = create_logger(app)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('xi4jzNEw02aKQ8NjLv6TGApBRYJQcl3UjUIrGB0zwWvkyXaiw5nbql3fYNM4DNp4Mqap4YrlUGolg6qCSskWv1O9LUtyGBnVBMiSSJQ4RRp4is95umkFxue9btIobuD7TUmXpfi/2WyJtwijkvfDnAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('f6d3bc464cfa5b571f225532ecbac1b1')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息

def yvideo(url = 'https://www.youtube.com/watch?v=qmeXgtzr-Xg'):
    search_url = 'https://qdownloader.io/download?url={}'.format(r.quote(url))
    request=r.Request(search_url, headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"})

    with r.urlopen(request) as response:
        data=response.read().decode("utf-8")
    import bs4
    soup = bs4.BeautifulSoup(data, "html.parser")
    t = soup.select('.col-md-8 td a' )
    url = t[0]['href']
    t = soup.select('.info.col-md-4 img' )
    img = t[0]['src']
    url = re.search(r'.*&title',url).group()[:-6]
    return url,img
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    client_msg = event.message.text
    def bn_message():
        message = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
                title='RE:0',
                text='雷姆超棒',
                thumbnail_image_url='https://cf.shopee.tw/file/ba20f2e96d5f8f6c0b386a077e21a020',
                actions=[
                    MessageTemplateAction(
                        label='要入教嗎?',
                        text='雷姆醒來了，萬歲'
                    )  ,
                        
                    URITemplateAction(
                        label='其他教(鬼滅)',
                        uri='https://www.youtube.com/watch?v=ikT1O4plOf4'
                    )  ,
                    PostbackTemplateAction(
                        label='postback',
                        text='postback text',
                        data='postback1'
                    ) ,  DatetimePickerTemplateAction(
                    label="請選擇日期",
                    # data= ,
                    data = "action = sell& mode=date",
                    mode='datetime',
                    initial='1990-01-01T10:00',
                    max='2019-03-10T00:00',
                    min='1930-01-01T23:59'
                )



                        ]
            )
                             )
        return message

    to = event.source.user_id
    if "文字" in  event.message.text :
        # line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))
        line_bot_api.push_message(to,StickerSendMessage(package_id=1, sticker_id=2))
        line_bot_api.push_message(to,StickerSendMessage(package_id=1, sticker_id=6))
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text= event.message.text ))
        line_bot_api.push_message(to, bn_message())
    elif event.message.text == "貼圖":
        line_bot_api.reply_message(event.reply_token,StickerSendMessage(package_id=1, sticker_id=2))
    elif event.message.text == "圖片":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url="https://cf.shopee.tw/file/ba20f2e96d5f8f6c0b386a077e21a020",
        # original_content_url是點進去看到的
        preview_image_url="https://i1.kknews.cc/SIG=3d9fkcp/s7300065054s67oqssq.jpg"))
        # preview_image_url是外面看到的
    elif event.message.text == "影片":

        line_bot_api.reply_message(event.reply_token , VideoSendMessage(original_content_url=yvideo()[0], preview_image_url=yvideo()[1]))
      

 
 
    # server_message=TextSendMessage(text="你是說"+client_msg+"嗎？")

    
    # line_bot_api.reply_message(event.reply_token, server_message2)
    # line_bot_api.reply_message(event.reply_token, server_message1)

    if '最新合作廠商' in client_msg:
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '最新活動訊息' in client_msg:
        message = bn_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '註冊會員' in client_msg:
        message = Confirm_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '旋轉木馬' in client_msg:
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '圖片畫廊' in client_msg:
        message = test()
        line_bot_api.reply_message(event.reply_token, message)
    elif '功能列表' in client_msg:
        message = function_list()
        line_bot_api.reply_message(event.reply_token, message)
    elif'按鈕' in client_msg: 
        buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='這是ButtonsTemplate',
            text='ButtonsTemplate可以傳送text,uri',
            thumbnail_image_url='https://cf.shopee.tw/file/ba20f2e96d5f8f6c0b386a077e21a020',
            actions=[
                MessageTemplateAction(
                    label='ButtonsTemplate',
                    text='ButtonsTemplate'
                ),
                URITemplateAction(
                    label='VIDEO1',
                    uri='https://www.youtube.com/watch?v=QIggvM6qEw8'
                ),
                PostbackTemplateAction(
                    label='postback',
                    text='postback text',
                    data='postback1'
                ),
                 DatetimePickerTemplateAction(
                    label="請選擇日",
                    data= "action = sell& mode=date",
                    mode='date',
                    initial='1990-01-01',
                    max='2019-03-10',
                    min='1930-01-01'
                ),
                
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token, buttons_template)
    else:
        message = TextSendMessage(text=client_msg)
        line_bot_api.reply_message(event.reply_token, message)

@handler.add(PostbackEvent) 
def handle_postback(event):
    to = event.source.user_id
    ts = event.postback.data
    dt = event.postback.params.get('datetime')
    dt = '日期為'+ dt.replace('T',' 時間為：')
    # dt = datetime.datetime.strptime(event.postback.params.get('datetime'),'%Y - %m - %dT %H:%M')
    # dt = dt.strftime('{d}%Y - %m - %d ,{t} %H:%M').format(d = '日期為：',t = '時間為：')
    line_bot_api.push_message(to, TextSendMessage(text= "回應是：\n"+dt))



import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
