from django.db import models


# Create your models here.
class Customer(models.Model):
    # 客户名
    name = models.CharField(max_length=200)

    # 电话号码
    phonenumber = models.CharField(max_length=200)

    # 地址
    address = models.CharField(max_length=200)

    # qq
    qq = models.CharField(max_length=20, null=True, blank=True)
