# -*- coding: UTF-8 -*-
import hashlib
import os
import random
import time
import json
import urllib

import cv2
from PIL import Image
from wechat_sdk import WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import TextMessage, ImageMessage, VoiceMessage, VideoMessage, LocationMessage
from wechatpy import WeChatClient

import requests
from django.http import HttpResponse

from HelloWorld.settings import STATIC_ROOT

WECHAT_TOKEN = 'cloudyang'
WEIXIN_APPID = 'wx1ceaf2b670549ad3'
WEIXIN_APPSECRET = 'dd3933b46ac5366786b16b8f70b847bc'

weChatClient = WeChatClient(access_token=WECHAT_TOKEN, appid=WEIXIN_APPID, secret=WEIXIN_APPSECRET)
wechat = WechatBasic(token=WECHAT_TOKEN, appid=WEIXIN_APPID, appsecret=WEIXIN_APPSECRET)

# wx token验证
def wx_verification(request):
    print(request.GET)
    if request.method == 'GET':
        # token 验证
        signature = request.GET['signature']
        echostr = request.GET['echostr']
        timestamp = request.GET['timestamp']
        nonce = request.GET['nonce']

        hashcode = token_verification(WECHAT_TOKEN,timestamp,nonce)
        print(hashcode)
        message = ''
        if hashcode==signature:
            message = echostr
        return HttpResponse(message)
    elif request.method == 'POST':
        wechat.parse_data(data=request.body)
        message = wechat.get_message()
        print('用户发送信息')
        print(message.type)
        if isinstance(message, TextMessage):
            # 文本消息 Content	文本消息内容
            context = message.content.strip()
            if context=='妖精' :
                print('上传妖精照片')
                # img = open('C:/Users/dell/Pictures/Saved Pictures/yaojing.jpg','rb')
                path = os.path.join(STATIC_ROOT, 'images/yaojing.jpg').replace('\\','/')
                img = open(path, 'rb')
                # print(type(img))
                we_img = wechat.upload_media(media_file=img,media_type='image')
                # print(we_img)
                result = wechat.response_image(we_img['media_id'])
                return HttpResponse(result,content_type='application/xml')
            elif context=='猫' :
                print('上传猫照片')
                # img = open('C:/Users/dell/Pictures/Saved Pictures/yaojing.jpg','rb')
                path = os.path.join(STATIC_ROOT, 'images/mao.jpg').replace('\\', '/')
                img = open(path, 'rb')
                we_img = wechat.upload_media(media_file=img, media_type='image')
                result = wechat.response_image(we_img['media_id'])
                return HttpResponse(result, content_type='application/xml')
            elif '色图' in context or '涩图' in context:
                dir_path = 'F:/data/images'
                filenames = os.listdir(dir_path)
                max_len = len(filenames)
                index = random.randint(0,max_len)
                filename = filenames.pop(index)
                path = dir_path+'/'+filename
                img = open(path, 'rb')
                we_img = wechat.upload_media(media_file=img, media_type='image')
                result = wechat.response_image(we_img['media_id'])
                return HttpResponse(result, content_type='application/xml')
            elif '天气' in context:
                context=context.replace('：',':')
                city_str = context.split(":").pop(1)
                result = wechat.response_text(weather(city_str))
                return HttpResponse(result, content_type='application/xml')
            result  = wechat.response_text(context)
            return HttpResponse(result, content_type='application/xml')
        elif isinstance(message, ImageMessage):
            # 图片消息 PicUrl	图片链接（由系统生成）
            piurl = message.picurl
            #MediaId	图片消息媒体id，可以调用获取临时素材接口拉取数据。
            mediaId = message.media_id
            # we_img = wechat.download_media(mediaId)
            print(piurl)
            changeId = change(piurl)
            result = wechat.response_image(changeId)
            return HttpResponse(result, content_type='application/xml')
        elif isinstance(message,VoiceMessage):
            # 语音消息 MediaId	语音消息媒体id，可以调用获取临时素材接口拉取数据。
            mediaId = message.media_id
            #Format	语音格式，如amr，speex等
            format = message.format
            #Recognition	语音识别结果，UTF8编码 【需要开通】
            recognition = message.recognition
            result = wechat.response_voice(mediaId)
            return HttpResponse(result, content_type='application/xml')
        elif isinstance(message,VideoMessage):
            # MediaId 视频消息媒体id，可以调用获取临时素材接口拉取数据。
            mediaId = message.media_id
            # ThumbMediaId 视频消息缩略图的媒体id，可以调用多媒体文件下载接口拉取数据。
            thumbMediaId = message.thumb_media_id
            result = wechat.response_voice(mediaId)
            return HttpResponse(result, content_type='application/xml')
        elif isinstance(message,LocationMessage):
            # Location_X	地理位置维度
            # Location_Y	地理位置经度
            location = message.location
            # Scale	地图缩放大小
            scale = message.scale
            # Label	地理位置信息
            label = message.label
            result = wechat.response_text(label)
            return HttpResponse(result, content_type='application/xml')



# 生成hashcode 对比
def token_verification(token, timestamp, nonce):
    list = [token, timestamp, nonce]
    list.sort()
    sha1 = hashlib.sha1()
    sha1.update(list[0].encode('utf-8'))
    sha1.update(list[1].encode('utf-8'))
    sha1.update(list[2].encode('utf-8'))
    hashcode = sha1.hexdigest()
    return hashcode


# 解析xml
def parse_xml(data):
    if len(data) == 0:
        return None
    # xmlData = ET.fromstring(data)
    # # 参数  描述
    # # ToUserName  接收方微信号
    # toUserName = xmlData.find('ToUserName').text
    # # FromUserName    发送方微信号，若为普通用户，则是一个OpenID
    # fromUserName = xmlData.find('FromUserName').text
    # # CreateTime  消息创建时间
    # createTime = xmlData.find('CreateTime').text
    # # MsgType 消息类型，链接为link
    # msgType = xmlData.find('MsgType').text
    # # Content	文本消息内容
    # content = xmlData.find('Content').text
    # # MsgId   消息id，64 位整型
    # msgId = xmlData.find('MsgId').text
    #
    # msg = {}
    # msg['ToUserName'] = toUserName
    # msg['FromUserName'] = fromUserName
    # msg['CreateTime'] = int(time.time())
    # msg['MsgType'] = msgType
    # msg['Content'] = content
    # return msg


# 格式化xml
def format_xml(toUserName, fromUserName, msgType,content):
    msg ={}
    msg['ToUserName'] = toUserName
    msg['FromUserName'] = fromUserName
    msg['CreateTime'] = int(time.time())
    msg['MsgType'] = msgType
    msg['Content'] = content
    XmlForm = '''
        <xml>
            <ToUserName><![CDATA[ToUserName]]></ToUserName>
            <FromUserName><![CDATA[FromUserName]]></FromUserName>
            <CreateTime><![CDATA[CreateTime]]></CreateTime>
            <MsgType><![CDATA[MsgType]]></MsgType>
            <Content><![CDATA[Content]]></Content>
        </xml>
    '''
    return XmlForm.format(msg)


def change(url):
    print('下载图片')
    name = 'images/cv2/'+ str(time.time()) + '.jpg'
    input_image_path = os.path.join(STATIC_ROOT, name).replace('\\', '/')
    output_image_path = input_image_path.replace(".jpg","-1.jpg")
    conn = urllib.request.urlopen(url)
    f = open(input_image_path, 'wb')
    f.write(conn.read())
    f.close()
    print('改变图片')
    cv_image(input_image_path,output_image_path)
    print('上传图片，返回id')
    img = open(output_image_path, 'rb')
    we_img = wechat.upload_media(media_file=img, media_type='image')
    return we_img['media_id']


def cv_image(input_image_path, output_image_path):
    img_rgb = cv2.imread(input_image_path)
    # 转化为灰度图
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    # 对原图进行模糊化
    img_gray = cv2.medianBlur(img_gray, 5)
    # 二值化操作
    img_edge = cv2.adaptiveThreshold(img_gray, 255,
                                     cv2.ADAPTIVE_THRESH_MEAN_C,
                                     cv2.THRESH_BINARY, blockSize=3, C=2)
    cv2.imwrite(output_image_path, img_edge)


def weather(city):
    print(city)
    filepath = os.path.join(STATIC_ROOT,'json/citycode.json')
    file = open(filepath,'r', encoding='UTF-8')
    city_json = json.load(file)
    city_code = "101010100"
    for item in city_json:
        if item['city_name'] == city:
            city_code = item['city_code']
            break

    url = 'http://t.weather.sojson.com/api/weather/city/'+city_code
    result = requests.get(url)

    content = result.content.decode()
    content_json = json.loads(content)
    print(content_json['data']['forecast'])
    forecast = content_json['data']['forecast']
    today = forecast.pop(0)
    message = today['ymd'] + '\r' + today['week'] + '\r' + today['high'] + ' ' + today['low'] + '\r' + today['type'] + '\r' + today['notice']
    return message

