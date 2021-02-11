# -*- coding: utf-8 -*-
# @Time    : 2021/2/11 下午4:59
# @Author  : void bug
# @FileName: views.py
# @Software: PyCharm
from django.shortcuts import render


def index(request):
    return render(request, "index.html", status=200)
