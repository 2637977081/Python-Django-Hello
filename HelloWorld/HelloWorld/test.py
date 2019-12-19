import json
import os
import urllib.request

import requests

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