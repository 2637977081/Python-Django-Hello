#19_陈宇航_信安1801

from django.contrib import admin
from  book_info.models import Cate, Book


# Register your models here.

class CateAdmin(admin.ModelAdmin):
    list_display =['id','name']

class BookAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'author', 'price','cate','picture']
    list_editable = ['name', 'author', 'price','cate']
    list_filter = ['cate']

admin.site.register(Cate,CateAdmin)
admin.site.register(Book,BookAdmin)