python : 3.10.5



pip install -i https://pypi.tuna.tsinghua.edu.cn/simple django==4.0.6

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple djangorestframework==3.13.1

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pymysql==1.0.2

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple django-cors-headers==3.13.0

pip install python-docx docx-mailmerge -i https://pypi.tuna.tsinghua.edu.cn/simple

查询端口使用情况
lsof -i:8000

python3 manage.py runserver 0.0.0.0:8000


打包成exe 进行分发

https://blog.csdn.net/qq_34809033/article/details/81873896

pip install pyinstaller

执行收集静态文件

python manage.py collectstatic

manage.spec 中添加打包的静态文件

​    datas=[(r'E:\CloudWorkSpace\EspectMain\DB_Server\VRITS\db_server\static_root',r'.\db_server\static_root'), (r'E:\CloudWorkSpace\EspectMain\DB_Server\VRITS\db_server\templates', r'.\db_server\templates')],

执行 python pyinstaller manage.spec -y打包exe

申请表填写
排水户名称
排水项目名称
填表日期
邮编/法定代表人
法定代表人手机
排水（建设）项目行政区和地址
总水
自来
自备
总排
含餐饮
其中生活污水量
处理方式
处理量
处理工艺
用地面积
总建筑面积
住宅
厂房
办公楼
餐饮
主要产品或服务
主要原料
建设工期
竣工日期
序号1
种类1
管径1
排水量1
路名、河道名1
有无1
序号2
种类2
管径2
排水量2
路名、河道名2
有无2
序号3
种类3
管径3
排水量3
路名、河道名3
有无3
序号4
种类4
管径4
排水量4
路名、河道名4
有无4
序号5
种类5
管径5
排水量5
路名、河道名5
有无5
序号6
种类6
管径6
排水量6
路名、河道名6
有无6
序号7
种类7
管径7
排水量7
路名、河道名7
有无7
序号8
种类8
管径8
排水量8
路名、河道名8
有无8
申请单位（承诺）
法定代表人（承诺）
竣工报告标题（报告）
承建项目（报告）
竣工日期（报告）
建筑层数（报告）

勾选排水设施
现场照片

( 1.有餐饮的排水户已建设规范的隔油池。
( 2.有厕所的排水户已建设规范的化粪池。
( 3.有洗车服务的排水户已建设规范的隔油沉淀池。
( 4.已按规定建设                的预处理设施。



applyer:"",
project:"",
date:"",
post_legal_representative:"",
cell_phone:"",
project_addr:"",
zongshui:"",
tap_water:"",
self_owned:"",
total_water:"",
total_catering:"",
domastic_wastewater:"",
process_method:"",
process_ammount:"",
process_technology:"",
site_area:"",
overall_floorage:"",
residence_area:"",
factory_area:"",
office_building_area:"",
catering_area:"",
main_product:"",
raw_material:"",
construction_period:"",
completion_date:"",

type_1:"",
pipe_diameter_1:"",
quantity_of_flow_1:"",
river_way_1:"",
have_or_not_1:"",

type_2:"",
pipe_diameter_2:"",
quantity_of_flow_2:"",
river_way_2:"",
have_or_not_2:"",

type_3:"",
pipe_diameter_3:"",
quantity_of_flow_3:"",
river_way_3:"",
have_or_not_3:"",

type_4:"",
pipe_diameter_4:"",
quantity_of_flow_4:"",
river_way_4:"",
have_or_not_4:"",

type_5:"",
pipe_diameter_5:"",
quantity_of_flow_5:"",
river_way_5:"",
have_or_not_5:"",

type_6:"",
pipe_diameter_6:"",
quantity_of_flow_6:"",
river_way_6:"",
have_or_not_6:"",

type_7:"",
pipe_diameter_7:"",
quantity_of_flow_7:"",
river_way_7:"",
have_or_not_7:"",

type_8:"",
pipe_diameter_8:"",
quantity_of_flow_8:"",
river_way_8:"",
have_or_not_8:"",

levels
drainage
