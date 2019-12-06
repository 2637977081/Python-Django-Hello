import os

from django import forms
from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.base import ContentFile
import time
import cv2

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
        image = request.FILES.get('image')
        image_path=STATIC_ROOT+'/images/'
        file_path = os.path.join(image_path, image.name)
        default_storage.save(file_path,ContentFile(image.read()))
        if username == 'admin' and password == '123456':
            to_html='success.html'
            context['username']=username
            context['image_first'] = STATIC_URL+"images/"+image.name
    return render(request, to_html, context)


def chang(request):
    to_html = 'success.html'
    context = {'message': 'error'}
    if request.method == 'POST':
        image_first = request.POST['image_per']
        context['image_first'] = image_first
        input_image_path = BASE_DIR+image_first
        image_second = image_first.replace('.',"_after.")
        output_image_path = BASE_DIR+image_second
        cv_image(input_image_path,output_image_path)
        context['image_second'] = image_second
    return render(request,to_html,context)


def cv_image(input_image_path,output_image_path):
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