# -*- coding: utf-8 -*-
from ast import Pass
from audioop import avg
import datetime
import json
import os
from django.db.models import Avg
from django.db.models import F
from django.db.models import Q
from django.forms.models import model_to_dict
from django.db.models import Avg, Max, Min, Count, Sum, IntegerField
from django.db.models.functions import Coalesce
import math
from collections import Counter

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_DIR = BASE_DIR + '/upload/'
# sys.path.append(BASE_DIR)

import time


from django.db import transaction
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
# from django.utils.http import urlquote

from db_server.models import *
from django.views.decorators.csrf import csrf_exempt

# 分页管理
from django.core.paginator import Paginator



def data_input(request): 
    if request.method == "GET":
        data = {}

        return render(request, 'data_input.html', data)


def data_input_com(request): 
    if request.method == "GET":
        data = {}

        return render(request, 'data_input_com.html', data)


def get_test_data(request): 
    if request.method == 'POST':
        Response = {}
        # json_result = json.loads(request.body)
        # account = json_result.get('account', "")  
        # print(json_result)


        try:
            pass


        except Exception as e:
            err_message = str(e)

            # 代码 0 其他错误，并把错误信息返回
            Response['code'] = 0
            Response['msg'] = err_message
            print(Response)
            return HttpResponse(json.dumps(Response))

        else:   # 代码无异常
            Response['code'] = 14000
            Response['msg'] = "密码成功重置为 123456 "
            print(Response)
            return HttpResponse(json.dumps(Response))