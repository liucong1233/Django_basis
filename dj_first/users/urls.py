from django.conf.urls import url, include
from . import views

urlpatterns = [
    # 每个路由信息都需要使用url函数来构造
    # url(路径,函数)
    url(r'^index/$', views.index),
]