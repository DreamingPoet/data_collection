# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import url


from . import data_service



urlpatterns = [

    path('data_input', data_service.data_input),
    path('data_input_com', data_service.data_input_com),
    path('get_test_data', data_service.get_test_data),
   
]