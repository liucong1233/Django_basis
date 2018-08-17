from django.http import HttpResponse
from django.shortcuts import render
from booktest.models import BookInfo


def index(request):
    """
    index视图
    :param request: 包含了请求信息对象
    :return: 响应对象
    """
    books = BookInfo.objects.all()

    return render(request, 'index.html', {"books": books})


