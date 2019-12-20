from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.template import Context, Template


def hello(request):
    return render(request, 'index.html', {'name': 'zyz'})


def book(request, cate_id):
    username = request.session.get('username')
    # if username is None:
    #     username = 'none'
    cate_list = Cate.objects.all()
    if cate_id == 0 or cate_id is None:
        book_list = Book.objects.all()
    else:
        # cate_list = Cate.objects.all()
        try:
            cate = Cate.objects.get(id=cate_id)
            book_list = Book.objects.filter(cate=cate)
        except:
            pass
    return render(request, 'book.html', locals())


def register(request):
    if request.method == "GET":
        return render(request, 'register.html', locals())
    elif request.method == "POST":
        user_name = request.POST.get("user_name", '')
        password = request.POST.get("password", '')
        if user_name != '' and password != '':
            if not User.objects.filter(username=user_name).exists():
                user = User.objects.create_user(username=user_name, password=password)
                user.save()
                # user.backend = 'django.contrib.auth.backends.ModelBackend'
                # login(request, user)
                # return redirect(request.session['login_from'], '/')
            return redirect('login')
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
                request.session['username'] = username
                return redirect('/book/0')
        else:
            errormsg = '用户名或密码错误!'
            return render(request, 'login.html', locals())


def log_out(request):
    try:
        logout(request)
    except Exception as e:
        print(e)
    return redirect(request.META['HTTP_REFERER'])


# 添加书籍
def book_add(request):
    if request.method == 'GET':
        return render(request, 'book_add.html', locals())
    elif request.method == 'POST':
        name = request.POST['name']
        author = request.POST['author']
        price = request.POST['price']
        cate = request.POST['cate']
        picture = request.POST['picture']
        try:
            # 查询是否存在该类别 get查询不到会报错
            cate_obj = Cate.objects.get(name=cate)
        except:
            # 不存在重新构建
            cate_obj = Cate(name=cate)

        # 最终都重新保存
        cate_obj.save()
        book_obj = Book(name=name, author=author, price=price, cate=cate_obj, picture=picture)
        book_obj.save()
        return redirect('/book/0/', locals())


# 删除书籍
def book_delete(request, book_id):
    book_obj = Book.objects.filter(id=book_id)
    book_obj.delete()
    return redirect('/book/0/', locals())


def cate_delete(request,cate_id):
    cate_obj = Cate.objects.filter(id=cate_id)
    cate_obj.delete()
    return redirect('/book/0/', locals())