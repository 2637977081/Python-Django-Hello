from django.db import models


class User(models.Model):

    id = models.AutoField(primary_key=True)
    appId = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    createTime = models.DateField(auto_now_add=True)
