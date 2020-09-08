import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class CommodityViews(View):
    def post(self,request):
        pass