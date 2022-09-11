# -*- coding: utf-8 -*-

import datetime
import json
import os

import math

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_DIR = BASE_DIR + '/upload/'
# sys.path.append(BASE_DIR)

import time

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
# from django.utils.http import urlquote

from django.views.decorators.csrf import csrf_exempt

from mailmerge import MailMerge

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

        try:
            data = request.POST
            file_dict = request.FILES.items()
            for (k, v) in file_dict:

                file_data = request.FILES.getlist(k)

                for index, fl in enumerate(file_data):
                    filename = fl._get_name()
                    print(index)
                    print(filename)
                    path_file = BASE_DIR + '/db_server/merge_file/temp/'
                    path_file += filename
                    with open(path_file, "wb") as f:
                        if fl.multiple_chunks():
                            for content in fl.chuncks():
                                f.write(content)
                        else:
                            data = fl.read()
                            f.write(data)
            


            # 获取模版文件
            document = MailMerge(BASE_DIR + '/db_server/merge_file/template.docx')

            # 将获取的数据设置到模版的域中
            document.merge(
                applyer= data.get("applyer"),
                project= data.get("project"),
                date= data.get("date"),
                post_legal_representative= data.get("post_legal_representative"),
                cell_phone= data.get("cell_phone"),
                project_addr= data.get("project_addr"),
                zongshui= data.get("zongshui"),
                tap_water= data.get("tap_water"),
                self_owned= data.get("self_owned"),
                total_water= data.get("total_water"),
                total_catering= data.get("total_catering"),
                domastic_wastewater= data.get("domastic_wastewater"),
                process_method= data.get("process_method"),
                process_ammount= data.get("process_ammount"),
                process_technology= data.get("process_technology"),
                site_area= data.get("site_area"),
                overall_floorage= data.get("overall_floorage"),
                residence_area= data.get("residence_area"),
                factory_area= data.get("factory_area"),
                office_building_area= data.get("office_building_area"),
                catering_area= data.get("catering_area"),
                main_product= data.get("main_product"),
                raw_material= data.get("raw_material"),
                construction_period= data.get("construction_period"),
                completion_date= data.get("completion_date"),

                type_1= data.get("type_1"),
                pipe_diameter_1= data.get("pipe_diameter_1"),
                quantity_of_flow_1= data.get("quantity_of_flow_1"),
                river_way_1= data.get("river_way_1"),
                have_or_not_1= data.get("have_or_not_1"),

                type_2= data.get("type_2"),
                pipe_diameter_2= data.get("pipe_diameter_2"),
                quantity_of_flow_2= data.get("quantity_of_flow_2"),
                river_way_2= data.get("river_way_2"),
                have_or_not_2= data.get("have_or_not_2"),

                type_3= data.get("type_3"),
                pipe_diameter_3= data.get("pipe_diameter_3"),
                quantity_of_flow_3= data.get("quantity_of_flow_3"),
                river_way_3= data.get("river_way_3"),
                have_or_not_3= data.get("have_or_not_3"),

                type_4= data.get("type_4"),
                pipe_diameter_4= data.get("pipe_diameter_4"),
                quantity_of_flow_4= data.get("quantity_of_flow_4"),
                river_way_4= data.get("river_way_4"),
                have_or_not_4= data.get("have_or_not_4"),

                type_5= data.get("type_5"),
                pipe_diameter_5= data.get("pipe_diameter_5"),
                quantity_of_flow_5= data.get("quantity_of_flow_5"),
                river_way_5= data.get("river_way_5"),
                have_or_not_5= data.get("have_or_not_5"),

                type_6= data.get("type_6"),
                pipe_diameter_6= data.get("pipe_diameter_6"),
                quantity_of_flow_6= data.get("quantity_of_flow_6"),
                river_way_6= data.get("river_way_6"),
                have_or_not_6= data.get("have_or_not_6"),

                type_7= data.get("type_7"),
                pipe_diameter_7= data.get("pipe_diameter_7"),
                quantity_of_flow_7= data.get("quantity_of_flow_7"),
                river_way_7= data.get("river_way_7"),
                have_or_not_7= data.get("have_or_not_7"),

                type_8= data.get("type_8"),
                pipe_diameter_8= data.get("pipe_diameter_8"),
                quantity_of_flow_8= data.get("quantity_of_flow_8"),
                river_way_8= data.get("river_way_8"),
                have_or_not_8= data.get("have_or_not_8"),

                levels= data.get("levels")
                )
            
            time_text = time.strftime("%Y%m%d%H%M%S", time.localtime())

            document.write(BASE_DIR + '/db_server/merge_file/temp/'+ time_text +'.docx')

        except Exception as e:
            err_message = str(e)

            # 代码 0 其他错误，并把错误信息返回
            Response['code'] = 0
            Response['msg'] = err_message

            return HttpResponse(json.dumps(Response))

        else:   # 代码无异常
            Response['code'] = 14000
            Response['msg'] = "成功"
            Response['url'] = "/db_server/download/" + time_text
            
            return HttpResponse(json.dumps(Response))


def download(request,id):
    if request.method == "GET":
        response = b''
        file_name = BASE_DIR + '/db_server/merge_file/temp/'+ id +'.docx'
        with open(file_name, 'rb') as file:
            response = HttpResponse(file,content_type='application/octet-stream')
            #文件流类型
            filename = id + ".docx"
            response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
            #表示带有文件附件，指定了文件名；浏览器会自动下载
            
        # os.remove(file_name)
        return response