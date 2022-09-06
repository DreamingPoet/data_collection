# -*- coding: utf-8 -*-
"""VRITS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from VRITS import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import static



urlpatterns = [

    # 登陆和注册
    # path('user_reg/', use_post.user_reg),
    # path('login/', use_post.login),

    # 数据录入
    path('db_server/', include('db_server.url')),


   
]