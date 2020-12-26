from flask import Flask, request, abort
# from flask.logging import create_logger
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


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
@handler.add(MessageEvent, message=TextMessage)
def bn_message():
    message = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='行事曆',
            text='雷姆超棒',
            thumbnail_image_url='https://cf.shopee.tw/file/ba20f2e96d5f8f6c0b386a077e21a020',
            actions=[
                MessageTemplateAction(
                    label='想要入教嗎?',
                    text='雷姆萬歲'
                ),

                URITemplateAction(
                    label='其他教',
                    uri='https://www.youtube.com/watch?v=ikT1O4plOf4'
                ),
                PostbackTemplateAction(
                    label='postback',
                    text='postback text',
                    data='postback1'
                ), DatetimePickerTemplateAction(
                    label="請選擇生日",
                    # data= ,
                    data="action = sell& mode=date",
                    mode='datetime',
                    initial='1990-01-01T10:00',
                    max='2019-03-10T00:00',
                    min='1930-01-01T23:59'
                )

            ]
        )
    )
    return message
@handler.add(MessageEvent, message=TextMessage)
def imagemap_message():
    message = ImagemapSendMessage(
        base_url="https://i.imgur.com/BfTFVDN.jpg",
        alt_text='最新的合作廠商有誰呢？',
        base_size=BaseSize(height=2000, width=2000),
        actions=[
            URIImagemapAction(
                #家樂福
                link_uri="https://tw.shop.com/search/%E5%AE%B6%E6%A8%82%E7%A6%8F",
                area=ImagemapArea(
                    x=0, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #生活市集
                link_uri="https://tw.shop.com/search/%E7%94%9F%E6%B4%BB%E5%B8%82%E9%9B%86",
                area=ImagemapArea(
                    x=1000, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #阿瘦皮鞋
                link_uri="https://tw.shop.com/search/%E9%98%BF%E7%98%A6%E7%9A%AE%E9%9E%8B",
                area=ImagemapArea(
                    x=0, y=1000, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #塔吉特千層蛋糕
                link_uri="https://tw.shop.com/search/%E5%A1%94%E5%90%89%E7%89%B9",
                area=ImagemapArea(
                    x=1000, y=1000, width=1000, height=500
                )
            ),
            URIImagemapAction(
                #亞尼克生乳捲
                link_uri="https://tw.shop.com/search/%E4%BA%9E%E5%B0%BC%E5%85%8B",
                area=ImagemapArea(
                    x=1000, y=1500, width=1000, height=500
                )
            )
        ]
    )
    return message

#TemplateSendMessage - ButtonsTemplate (按鈕介面訊息)
@handler.add(MessageEvent, message=TextMessage)
def buttons_message():
    message = TemplateSendMessage(
        alt_text='好消息來囉～',
        template=ButtonsTemplate(
            thumbnail_image_url="https://pic2.zhimg.com/v2-de4b8114e8408d5265503c8b41f59f85_b.jpg",
            title="是否要進行抽獎活動？",
            text="輸入生日後即獲得抽獎機會",
            actions=[
                DatetimePickerTemplateAction(
                    label="請選擇生日",
                    data="input_birthday",
                    mode='date',
                    initial='1990-01-01',
                    max='2019-03-10',
                    min='1930-01-01'
                ),
                MessageTemplateAction(
                    label="看抽獎品項",
                    text="有哪些抽獎品項呢？"
                ),
                URITemplateAction(
                    label="免費註冊享回饋",
                    uri="https://tw.shop.com/nbts/create-myaccount.xhtml?returnurl=https%3A%2F%2Ftw.shop.com%2F"
                )
            ]
        )
    )
    return message

#TemplateSendMessage - ConfirmTemplate(確認介面訊息)
@handler.add(MessageEvent, message=TextMessage)
def Confirm_Template():

    message = TemplateSendMessage(
        alt_text='是否註冊成為會員？',
        template=ConfirmTemplate(
            text="是否註冊成為會員？",
            actions=[
                PostbackTemplateAction(
                    label="馬上註冊",
                    text="現在、立刻、馬上",
                    data="會員註冊"
                ),
                MessageTemplateAction(
                    label="查詢其他功能",
                    text="查詢其他功能"
                )
            ]
        )
    )
    return message

#旋轉木馬按鈕訊息介面
@handler.add(MessageEvent, message=TextMessage)
def Carousel_Template():
    message = TemplateSendMessage(
        alt_text='一則旋轉木馬按鈕訊息',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Number_1_in_green_rounded_square.svg/200px-Number_1_in_green_rounded_square.svg.png',
                    title='這是第一塊模板',
                    text='一個模板可以有三個按鈕',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='將這個訊息偷偷回傳給機器人'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是1'
                        ),
                        URITemplateAction(
                            label='進入1的網頁',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Number_1_in_green_rounded_square.svg/200px-Number_1_in_green_rounded_square.svg.png'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuo7n2_HNSFuT3T7Z9PUZmn1SDM6G6-iXfRC3FxdGTj7X1Wr0RzA',
                    title='這是第二塊模板',
                    text='副標題可以自己改',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=2'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是2'
                        ),
                        URITemplateAction(
                            label='進入2的網頁',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Number_2_in_light_blue_rounded_square.svg/200px-Number_2_in_light_blue_rounded_square.svg.png'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png',
                    title='這是第三個模塊',
                    text='最多可以放十個',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=3'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是3'
                        ),
                        URITemplateAction(
                            label='uri2',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png'
                        )
                    ]
                )
            ]
        )
    )
    return message

#TemplateSendMessage - ImageCarouselTemplate(圖片旋轉木馬)
@handler.add(MessageEvent, message=TextMessage)
def image_carousel_message1():
    message = TemplateSendMessage(
        alt_text='圖片旋轉木馬',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/uKYgfVs.jpg",
                    action=URITemplateAction(
                        label="跳崖",
                        uri="https://images.alphacoders.com/700/thumb-1920-700998.png"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QOcAvjt.jpg",
                    action=URITemplateAction(
                        label="愛米利亞",
                        uri="https://images.alphacoders.com/692/thumb-350-692362.png"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/Np7eFyj.jpg",
                    action=URITemplateAction(
                        label="486",
                        uri="https://images6.alphacoders.com/718/thumb-1920-718319.png"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QRIa5Dz.jpg",
                    action=URITemplateAction(
                        label="雷姆",
                        uri="https://images6.alphacoders.com/724/thumb-1920-724058.jpg"
                    )
                )
            ]
        )
    )
    return message
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    client_msg = event.message.text
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


    #
    # elif event.message.text == "影片":
    #
    #     line_bot_api.reply_message(event.reply_token,VideoSendMessage(original_content_url= yt.yvideo()[0], preview_image_url= 'https://i1.kknews.cc/SIG=3d9fkcp/s7300065054s67oqssq.jpg'))




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
        # message = function_list()
        message = image_carousel_message1()
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
    dt = '日期為'+ dt.replace('T', ' 時間為：')
    # dt = datetime.datetime.strptime(event.postback.params.get('datetime'),'%Y - %m - %dT %H:%M')
    # dt = dt.strftime('{d}%Y - %m - %d ,{t} %H:%M').format(d = '日期為：',t = '時間為：')
    line_bot_api.push_message(to, TextSendMessage(text= "回應是：\n"+dt))



import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
