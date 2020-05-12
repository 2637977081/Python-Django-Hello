# -*- coding: UTF-8 -*-
import hashlib
import os
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django import forms
from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.base import ContentFile
import time
import cv2
import smtplib

from HelloWorld.settings import STATIC_URL, STATICFILES_DIRS, STATIC_ROOT, BASE_DIR


def hello(request):
    return HttpResponse("Hello World!")


def helloHtml(request):
    context = {}
    context['title'] = 'hello world!'
    context['time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return render(request, 'hello.html', context)


# 访问登录页
def login_page(request):
    return render(request, 'login.html')


# 登录提交按钮
def login(request):
    context = {'message': 'error'}
    to_html = 'error.html'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == 'admin' and password == '123456':
            to_html = 'success.html'
            context['username'] = username
    return render(request, to_html, context)


def chang(request):
    to_html = 'success.html'
    context = {'message': 'error'}
    if request.method == 'POST':
        image = request.FILES.get('imagePer')
        image_path = os.path.join(STATIC_URL + 'images/')
        image_first = os.path.join(image_path, image.name)
        input_image_path = BASE_DIR + image_first
        default_storage.save(input_image_path, ContentFile(image.read()))
        image_second = image_first.replace('.', "_after.")
        output_image_path = BASE_DIR + image_second
        cv_image(input_image_path, output_image_path)
        context['image_first'] = image_first
        context['image_second'] = image_second
    return render(request, to_html, context)


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


def send_email(request):
    receivers = ['tdmdm@foxmail.com', '1535274781@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    if request.POST['receiver'] != '':
        receivers.append(request.POST['receiver'])
    # 获取文件
    image_first = request.POST['image_send_one']
    image_first_path = BASE_DIR + image_first
    image_second = request.POST['image_send_two']
    image_second_path = BASE_DIR + image_second
    email_fun(image_first_path,image_second_path,receivers)
    return HttpResponse("发送成功!")


def email_fun(image_first_path,image_second_path,receivers):
    # 第三方 SMTP 服务
    # mail_host = "smtp.sina.com"  # 设置服务器
    mail_host = "smtp.qq.com"  # 设置服务器
    # mail_user = "catcoder@sina.com"  # 用户名
    mail_user = "2637977081@qq.com"  # 用户名
    # mail_pass = "0eff24ba4cfa6935"  # sina口令
    mail_pass = "nmyvwpiitwzuebej"  # qq口令

    sender = '2637977081@qq.com'

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
    att2["Content-Disposition"] = 'attachment; filename="mao.jpg"'
    message.attach(att2)

    try:
        smtpObj = smtplib.SMTP(mail_host)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

def cat(request):
    return render(request, 'cat.html')