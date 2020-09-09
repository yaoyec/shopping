from django.db import models

# Create your models here.
class User(models.Model):
    phone = models.IntegerField('账号',max_length=11)
    password = models.CharField("密码", max_length=10)

