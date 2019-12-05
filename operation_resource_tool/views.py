import os

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from openpyxl import load_workbook

from kbd_aps_data_tool import settings
from operation_resource_tool.common import ResponseMessage, render_json

from django.shortcuts import render, redirect
from operation_resource_tool.models.upload_file import UploadFile
from datetime import datetime

def index(request):
    # return render(request, 'index.html')
    return redirect('converter')


def converter(request):
    context = {
        'files': {
        },
        'upload_message': request.GET.get('upload_message', ''),
        'convert_message': request.GET.get('convert_message', '')
    }
    for type in ['product_attribute','item_project']:
        context['files'][type]=[ {'name':file.name, 'value':file.pathname} for file in UploadFile.objects.filter(type=type).order_by('-id')[0:15]]
    
    return render(request, 'converter.html', context=context)


def converter_upload(request):
    if request.FILES == None or len(request.FILES) <= 0:
        return redirect(reverse('converter') + '?upload_message=文件不能为空')
    for filetype, file in request.FILES.items():
        if file.content_type != 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            return redirect(reverse('converter') + '?upload_message=请上传EXCEL文件,文件类型为.xlsx')
        else:
            name = '%s_%s' % (datetime.strftime(datetime.now(),'%y%m%d%H%M%S'), file.name)
            path = os.path.join('medias','input')
            pathname=os.path.join(path,name)
            print(file.__dict__)
            with open(pathname, '+wb') as wfile:
                for chunk in file.chunks():
                    wfile.write(chunk)

            ufile = UploadFile(origin_name=file.name,
                              type=filetype,
                              name = name,
                              pathname = pathname,
                              created_at=datetime.now())
            ufile.save()
    return redirect(reverse('converter')+'?upload_message=上传成功')        

def convert(request):
    project_attribute = '/home/chen/Desktop/kbd_aps_data_tool/medias/机种属性.xlsx'
    item_project = '/home/chen/Desktop/kbd_aps_data_tool/medias/物料机种.xlsx'
    project_attribute_wb = load_workbook(project_attribute)
    item_project_wb = load_workbook(item_project)
    sheet1 = project_attribute_wb[project_attribute_wb.sheetnames[0]]
    sheet2 = item_project_wb[item_project_wb.sheetnames[0]]
    # 表总行数
    max_row = sheet2.max_row
    # 表总列数
    max_col = 4
    item_project_dict = {}
    for x in range(1, max_row+1):
        for y in range(1,max_col+1):
            # 获取表中x行y列的值
            cell_data = sheet2.cell(row=x, column=y).value
            if cell_data:

                if x == 1:
                    item_project_dict[y] = [cell_data]
                else:
                    item_project_dict[y].append(cell_data)
    max_row1 = sheet1.max_row
    max_col1 = 7
    project_attribute_dict = {}
    for x in range(1, max_row1+1):
        for y in range(1,max_col1+1):
            # 获取表中x行y列的值
            cell_data = sheet1.cell(row=x, column=y).value
            if cell_data:

                if x == 1:
                    project_attribute_dict[y] = [cell_data]
                else:
                    project_attribute_dict[y].append(cell_data)
    for v in item_project_dict.values():
        pass
    for m in project_attribute_dict:
        pass
    return render(request, 'convert_result.html', context={'message': '处理成功'})
