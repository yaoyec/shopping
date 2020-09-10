import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from commodity.models import Commodity
from .models import Commodity_images
# Create your views here.
from django.views import View


class CommodityViews(View):
    def post(self, request):
        pass

    def get(self, request, cname):
        if cname:
            try:
                shopping = Commodity.objects.get(cname=cname)
            except Exception as e:
                print('灭有该商品的详细信息%s' % e)
                result = {'code': 1001, 'error': 'No such goods'}
                return JsonResponse(result)

            cname = shopping.cname  # 商品名称
            price = shopping.price  # 商品价格
            category = shopping.category  # 商品类别
            description = shopping.description  # 商品描述
            com_id = shopping.id  # 商品的id
            # 通过商品的id 来找他的图片
            images = Commodity_images.objects.filter(com = com_id)
            result = {'cname':cname,'price':price,'category':category,'description':description,'images':images}

            return JsonResponse(result)
