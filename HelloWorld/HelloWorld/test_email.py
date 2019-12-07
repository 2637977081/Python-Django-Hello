#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 第三方 SMTP 服务
# mail_host = "smtp.sina.com"  # 设置服务器
mail_host = "smtp.qq.com"  # 设置服务器
# mail_user = "catcoder@sina.com"  # 用户名
mail_user = "2637977081@qq.com"  # 用户名
# mail_pass = "0eff24ba4cfa6935"  # sina口令
mail_pass = "nmyvwpiitwzuebej"  # qq口令

sender = '2637977081@qq.com'
receivers = ['2637977081@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

image_first_path = 'D:/python/workspace-django/HelloWorld/static/images/yaojing.jpg'
image_second_path = 'D:/python/workspace-django/HelloWorld/static/images/lvgang.jpg'

# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header(sender)  # 搜狐邮箱规定发送者与from相同
message['To'] = Header("可爱的你(*╹▽╹*))", 'utf-8')
message['Subject'] = Header('你好(*´▽｀)ノノ', 'utf-8')
# 邮件正文内容
message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open(image_first_path, 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="yaojing.jpg"'
message.attach(att1)

# 构造附件2，传送当前目录下的 runoob.txt 文件
att2 = MIMEText(open(image_second_path, 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="lvgang.jpg"'
message.attach(att2)

try:
    smtpObj = smtplib.SMTP(mail_host)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")