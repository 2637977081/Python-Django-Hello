from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.template import Context, Template


def hello(request):
    return render(request, 'index.html', {'name': 'zyz'})


def book(request, cate_id):
    cate_list = Cate.objects.all()
    cate = Cate.objects.get(id=cate_id)
    book_list = Book.objects.filter(cate=cate)
    return render(request, 'book.html', locals())


def register(request):
    if request.method == "GET":
        return render(request, 'register.html', locals())
    elif request.method == "POST":
        user_name = request.POST.get("user_name", '')
        password = request.POST.get("password", '')
        if user_name != '' and password != '':
            if User.objects.filter(username=user_name).exists() == False:
               user = User.objects.create_user(username=user_name, password=password)
               user.save()
               # user.backend = 'django.contrib.auth.backends.ModelBackend'
               # login(request, user)
               # return redirect(request.session['login_from'], '/')
            return HttpResponseRedirect('login.')
        else:
            return render(request, 'register.html')


def log_in(request):
    if request.method == 'GET':
        return render(request, 'login.html', locals())
    elif request.method == 'POST':
        username = request.POST.get("user_name", '')
        password = request.POST.get("password", '')
        if username != '' and password != '':
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print("登录成功!")
                return render(request, 'book.html', locals())
        else:
            errormsg = '用户名或密码错误!'
            return render(request, 'login.html', locals())



def log_out(request):
    try:
        logout(request)
    except Exception as e:
        print(e)
    return redirect(request.META['HTTP_REFERER'])
