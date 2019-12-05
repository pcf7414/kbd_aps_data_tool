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
    return render(request, 'convert_result.html', context={'message': '处理成功'})
