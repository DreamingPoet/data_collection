python : 3.10.5



pip install -i https://pypi.tuna.tsinghua.edu.cn/simple django==4.0.6

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple djangorestframework==3.13.1

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pymysql==1.0.2

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple django-cors-headers==3.13.0

pip install python-docx docx-mailmerge -i https://pypi.tuna.tsinghua.edu.cn/simple

pip install pillow -i https://pypi.tuna.tsinghua.edu.cn/simple

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



如何用JS有效的压缩图片
https://www.jb51.net/article/212682.htm



使用formdata在vue和django之间传递文件
在前端页面中如果有文件或者图片需要上传的场景下，通用做法是使用formdata将文件从前端传输到后台，在后台上传文件并将url保存在数据库。
当前项目是使用vue + Element UI + django 的框架，需要将文件从vue传递到django中，上传阿里云OSS存储。记录使用方法

formdata的简单使用
创建
新建一个formdata的变量

var data = new FormData() 
    data.append('name', this.createForm.name)
    data.append('desc', this.createForm.desc)
    data.append('page_url', this.createForm.page_url)
    data.append('edit', this.createForm.edit)
    data.append('page_id', this.createForm.page_id)
添加数据
通过append(key, value)来添加数据，这里分为两种情况，
一、key值无重复
key值不存在重复的情况下，一个key对应一个value

data.append('name', this.createForm.name)
data.append('desc', this.createForm.desc)
二、key值重复
key值在某些时候会重复，如上传多个文件时，这时一个key对应一个数组，数组中为多个value

data.append('file', file.raw)
data.append('file', file.raw)
获取数据
key值对应一个value，可以通过get方法取值

data.get(key)
key值对应多个value，可以通过getAll方法取值

data.getAll(key)
如果key对应多个value而使用get取值，只能取到value的最后一个值

判断数据是否存在
我们可以通过has(key)来判断是否对应的key值

data.has('name')
删除数据
通过delete(key)，来删除数据

data.delete('name')
遍历数据
我们可以通过entries()来获取一个迭代器，然后遍历所有的数据，

formData.append("k1", "v1");
formData.append("k1", "v2");
formData.append("k2", "v1");
 
var i = formData.entries();
 
i.next(); // {done:false, value:["k1", "v1"]}
i.next(); // {done:fase, value:["k1", "v2"]}
i.next(); // {done:fase, value:["k2", "v1"]}
i.next(); // {done:true, value:undefined}
项目中使用
要完成的功能如下，在一个弹出框中能够输入信息，重点是能够添加多个文件。



在Element UI中已经处理好，当选择多个文件之后，会保存到一个数组中，我只需要对这个数组操作即可。

vue代码
创建formdata
var data = new FormData();
// 普通变量
data.append('name', this.createForm.name)
data.append('desc', this.createForm.desc)
data.append('page_url', this.createForm.page_url)
data.append('edit', this.createForm.edit)
data.append('page_id', this.createForm.page_id)

// 文件。因为涉及到编辑功能，所以对于新上传的文件保存其`file.raw`，编辑的文件保存文件id
this.createForm.file.forEach((file) => {
  if (file.raw) {
    data.append('new_files', file.raw)
  }else{
    data.append('old_files', file.page_file_id)
  }
})
pageCreate(data).then((res) => {
........
}
}
发送请求

export function pageCreate(form) {
    return postForm(URL.createUrl, form)
}
post请求的内容格式。post请求不是普通的json而是form-data

export function postForm (url, data= {}) {
  return new Promise((resolve, reject) => {
    axios.create({
      withCredentials: true,
      headers: {'X-CSRFToken': getCookie('csrftoken'), 'Content-Type':  "multipart/form-data"},
    }).post(url, data).then(response => {
      resolve(response.data)
    }, err => {
      reject(err)
    })
  })
}
后端处理
django的接收：

# 接收到formdata的出文件之外的数据
data = request.POST

# 接收文件，getlist是接收多个文件
# formdata在vue中同一个key传入了多个value，value成为了一个数组，所以需要使用getlist来获取所有文件
new_files = request.FILES.getlist('new_files')


# formdata在vue中同一个key只有一个文件类型的value，可以使用get来获取文件
new_files = request.FILES.get('file')
后续将文件上传到阿里云的对象存储，将文件的url保存到数据库。展示或编辑文件时，只需要传入文件的url，element UI即可解析出文件。











python-docx设置表格对齐方式
https://baijiahao.baidu.com/s?id=1664476132973597291&wfr=spider&for=pc

小梁学编程

2020-04-20 17:17
关注
在Word文档中表格中对齐方式的设置可以分为表格的对齐方式和单元格的对齐方式，可以通过“开始”菜单栏中的“段落”中设置表格的对齐方式，可以通过“布局”菜单栏中的“对齐方式”中设置单元格的对齐方式。


表格对齐方式设置

单元格对齐方式设置
而在python-docx包中要使用table.alignment、cell.vertical_alignment和paragraph.alignment进行设置，笔者总结了python-docx包中表格和单元格等2种设置对齐方式，并在文章最后将文章主要内容制作了思维导图。

01
表格的对齐方式
在设置表格的对齐中，将表格作为一个整体，要用到table的alignment属性。python-docx包定义了表格对齐的枚举类型，存储在docx.enum.table import WD_TABLE_ALIGNMENT中，共定义了LEFT、CENTER和RIGHT三个常量。含义如下

WD_TABLE_ALIGNMENT.LEFT ：表格为左对齐
WD_TABLE_ALIGNMENT.CENTER：表格为居中对齐
WD_TABLE_ALIGNMENT.RIGHT：表格为右对齐
本文以LFET为例说明表格对齐方式的设置过程，见代码：

from docx import Document # 导入docx
from docx.enum.table import WD_TABLE_ALIGNMENT # 导入表格对齐方式
from docx.shared import Cm # 导入单位转换函数
document = Document() # 新建docx文档
table = document.add_table(3, 3) # 添加表格1
table.alignment = WD_TABLE_ALIGNMENT.LEFT # 设置表格为右对齐
for col in table.columns: # 表格1设置列宽为2cm，便于演示，与设置无关
for cell in col.cells:
cell.width = Cm(2)
document.save('test.docx')
表格的左对齐效果见下图


表格左对齐效果图
同理，将第6行代码分别设置为居中和右对齐，见如下代码，运行后表格的效果见下图。

table.alignment = WD_TABLE_ALIGNMENT.CENTER # 设置表格为居中对齐
table.alignment = WD_TABLE_ALIGNMENT.RIGHT # 设置表格为右对齐


表格居中对齐效果图

表格右对齐效果图
02
单元格的对齐方式
在对单元格对齐方式设置的时候，将单元格视为一个整体，要使用单元格中的垂直对齐（cell.vertical_alignment）和单元格中的段落的对齐（paragraph.alignment）等2种对齐方式配合使用。在docx.enum.table .WD_ALIGN_VERTICAL定义了TOP、CENTER和BOTTOM等3种类型，含义如下：

WD_CELL_VERTICAL_ALIGNMENT.TOP：单元格内容靠上对齐
WD_CELL_VERTICAL_ALIGNMENT.CENTER：单元格内容居中对齐
WD_CELL_VERTICAL_ALIGNMENT.BOTTOM：单元格内容靠下对齐
在WD_PARAGRAPH_ALIGNMENT中定义了4中类型，分别是LEFT、CENTER、RIGHT和JUSTIFY等4中类型，含义如下：

WD_PARAGRAPH_ALIGNMENT.LEFT：段落左对齐
WD_PARAGRAPH_ALIGNMENT.CENTER：段落居中对齐
WD_PARAGRAPH_ALIGNMENT.RIGHT：段落右对齐
WD_PARAGRAPH_ALIGNMENT.JUSTIFY：段落两端对齐
关于段落的设置可以参考文章python-docx段落设置。在单元格垂直对齐和段落对齐的配合过程中可以组合成12种方式，分别是：靠上两端对齐、靠上居中对齐、靠上右对齐、中部两端对齐、中部居中对齐、中部右对齐、靠下两端对齐、靠下居中对齐、靠下右对齐、靠上左对齐、中部左对齐、靠下左对齐。其中，在WORD软件中内置了前9种对齐方式。这9种对齐方式的设置代码如下：

from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT # 导入单元格垂直对齐
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT # 导入段落对齐
document = Document()
table = document.add_table(3, 3) # 添加表格1
for row in table.rows:
row.height = Cm(3) # 设置表格行高为3cm，便于演示，与设置对齐无关
cell = table.cell(0,0)
cell.text = "靠上两端对齐"
cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP
cell.paragraphs[0].alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
cell = table.cell(0,1)
cell.text = "靠上居中对齐"
cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP
cell.paragraphs[0].alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
cell = table.cell(0,2)
cell.text = "靠上右对齐"
cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP
cell.paragraphs[0].alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT
cell = table.cell(1,0)
cell.text = "中部两端对齐"
cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
cell.paragraphs[0].alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
cell = table.cell(1,1)
cell.text = "中部居中对齐"
cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
cell.paragraphs[0].alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
cell = table.cell(1,2)
cell.text = "中部右对齐"
cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
cell.paragraphs[0].alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT
cell = table.cell(2,0)
cell.text = "靠下两端对齐"
cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.BOTTOM
cell.paragraphs[0].alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
cell = table.cell(2,1)
cell.text = "考下中部对齐"
cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.BOTTOM
cell.paragraphs[0].alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
cell = table.cell(2,2)
cell.text = "靠下右对齐"
cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.BOTTOM
cell.paragraphs[0].alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT
运行效果见下图：


9种对齐方式与WORD软件中对应图
另外三种的设置可以参考上述代码。

笔者总结了python-docx包中对表格和单元格的对齐方式，制作了思维导图见下图。希望对使用python-docx包设置docx表格对齐时提供参考。

