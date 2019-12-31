import json
import os
import random
import urllib.request
from io import BytesIO

import requests
from PIL import Image
from wechat_sdk import WechatBasic

from HelloWorld.settings import STATIC_ROOT

# url='https://raw.githubusercontent.com/baichengzhou/weather.api/master/src/main/resources/citycode-2019-08-23.json'
# path = os.path.join(STATIC_ROOT,'json/citycode.json').replace('\\', '/')
# conn = urllib.request.urlopen(url)
# f = open(path, 'wb')
# f.write(conn.read())
# f.close()
#
# context = '天气:武汉'
# weather_str = context.split(':').pop(0)
# city_str = context.split(":").pop(1)
#
# city_code = "101010100"
# url = 'http://t.weather.sojson.com/api/weather/city/' + city_code
# result = requests.get(url)
#
# content = result.content.decode()
# content_json = json.loads(content)
# print(content_json['data']['forecast'])
# forecast = content_json['data']['forecast']
# today = forecast.pop(0)
# message = today['ymd']+'\r'+today['week'] +'\r'+today['high']+' '+today['low']+'\r'+today['type'] + '\r' +today['notice']


# WECHAT_TOKEN = 'cloudyang'
# WEIXIN_APPID = 'wx1ceaf2b670549ad3'
# WEIXIN_APPSECRET = 'dd3933b46ac5366786b16b8f70b847bc'
#
# wechat = WechatBasic(token=WECHAT_TOKEN, appid=WEIXIN_APPID, appsecret=WEIXIN_APPSECRET)
#
# path = os.path.join(STATIC_ROOT, 'images/mao.jpg').replace('\\', '/')
# img = open(path, 'rb')
# we_img = wechat.upload_media(media_file=img, media_type='image')
# we_img_bytes = wechat.download_media(we_img['media_id'])
# image = Image.open(StringIO.StringIO(we_img_bytes.content))
# bytes_stream = BytesIO(we_img_bytes.content)
# img_file = Image.open(bytes_stream)
# print(type(img_file))

# WECHAT_TOKEN = 'cloudyang'
# WEIXIN_APPID = 'wx1ceaf2b670549ad3'
# WEIXIN_APPSECRET = 'dd3933b46ac5366786b16b8f70b847bc'
#
# url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid='+WEIXIN_APPID+'&secret='+WEIXIN_APPSECRET
# result = requests.get(url)
# content = result.content.decode()
# content_json = json.loads(content)
# token = content_json ['access_token']
#
# url = 'https://api.weixin.qq.com/cgi-bin/user/get?access_token='+token+'&scope=snsapi_base'
# result = requests.get(url)
# print(result)

# import HelloWorld.wx as wx

# wx.love_say()
