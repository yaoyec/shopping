from django.db import models

# Create your models here.
class Commodity(models.Model):
    cname = models.CharField("商品名",max_length=10)
    price = models.DecimalField("商品价格",max_digits=7,decimal_places=2)
    category=models.CharField("商品类别",max_length=10)
    description = models.TextField("商品描述")


class Commodity_images(models.Model):
    bimages = models.ImageField('商品图片', null=True)
    com = models.ForeignKey(Commodity, on_delete=models.CASCADE, null=True)
