
import os

from django.http import HttpResponse
from django.shortcuts import render,redirect
from openpyxl import load_workbook

from kbd_aps_data_tool import settings
from operation_resource_tool.common import ResponseMessage, render_json



from django.shortcuts import render, redirect


def index(request):
    # return render(request, 'index.html')
    return redirect('converter')



def converter(request):
    context = {'files': {
        'product_attribute': [{'name': 'a.xlsx', 'value': 'data/a-uuid.a.xlsx'}],
        'item_project': [{'name': 'a.xlsx', 'value': 'data/a-uuid.a.xlsx'}]
    }}
    return render(request, 'converter.html', context=context)


def converter_upload(request):
    files = request.FILES.getlist("file")
    if files == None or len(files) <= 0:
        return HttpResponse('文件不能为空',status=400)
    for file in files:
        if file.content_type != 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            return HttpResponse('请上传EXCEL文件,文件类型为.xlsx', status=400)
        else:
            wb = load_workbook(filename=file, read_only=True, data_only=True)
            path = os.path.join(settings.BASE_DIR, 'output')
            if not os.path.exists(path):
                os.makedirs(path, exist_ok=True)
            filepath = os.path.join(path, file)
            wb.save(filepath)
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


# def converter_upload(request):
#     files = request.FILES
#     return redirect('converter')

