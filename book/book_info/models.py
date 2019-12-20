#19_陈宇航_信安1801

from django.db import models
import time
# Create your models here.
class Cate(models.Model) :
    name = models.CharField(verbose_name = '分类名称',max_length = 20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "图书分类"
        verbose_name_plural = verbose_name

def get_img_path(instance,filename):
    str_current_time = str(time.time()).replace("." , '')
    return 'upload/{0}{1}'.format(str_current_time , filename)

class Book(models.Model):
    name = models.CharField(verbose_name = "图书名称",max_length = 30)
    author = models.CharField(verbose_name = "作者",max_length = 20)
    price = models.FloatField(verbose_name = "价格")
    cate = models.ForeignKey(Cate,verbose_name = "分类",on_delete = models.CASCADE)
    picture = models.ImageField(verbose_name = "图书封面",upload_to = get_img_path,null = True)

    def __str__(self):
        return  self.name

    class Meta:
        verbose_name = "图书"
        verbose_name_plural = verbose_name