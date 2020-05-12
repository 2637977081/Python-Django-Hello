import win32gui
import win32con
import win32clipboard as w
import random
import time
import requests
import json


def joke_text():
    time_rand = random.randint(0, 3600)
    time_str = str(int(time.time()) - time_rand)
    page_rand = random.randint(1, 20)
    page_str = str(page_rand)
    url = 'http://v.juhe.cn/joke/content/list.php?key=7b9a08d5c9f1439d060a57428a360ec5&page=' + page_str + '&pagesize=1' \
                                                                                                           '&sort=desc' \
                                                                                                           '&time=' + time_str
    print(url)
    result = requests.get(url)
    content = result.content.decode()
    content_json = json.loads(content)
    print(content_json)
    message = content_json['result']['data'].pop(0)['content']
    return message


# 发送的消息
msg = joke_text()
# 窗口名字
name = "卢 本 伟 广 场"
# 将测试消息复制到剪切板中
w.OpenClipboard()
w.EmptyClipboard()
w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
w.CloseClipboard()
# 获取窗口句柄
handle = win32gui.FindWindow(None, name)
while 1 == 1:
    # if 1 == 1:
    # 填充消息
    time.sleep(3000)
    win32gui.SendMessage(handle, 770, 0, 0)
    # 回车发送消息
    win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
