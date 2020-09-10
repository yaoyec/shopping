from django.urls import path
from . import views
urlpatterns=[
    path('index',views.CommodityViews.as_view()),
    path('<int:index>',views.CommodityViews.as_view()),
]