
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
    return render(request, 'convert_result.html', context={'message': '处理成功'})


# def converter_upload(request):
#     files = request.FILES
#     return redirect('converter')

