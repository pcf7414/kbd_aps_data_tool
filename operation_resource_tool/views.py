from django.shortcuts import render

from operation_resource_tool.common import ResponseMessage, render_json


def index(request):
    return render(request, 'index.html')

def init_data(request):
    # message = ResponseMessage()
    message = {
        'result':True,
        'content':{'item_project':[{'name':'物料机种1','value':'物料机种1url'}],
        'project_attribute':[{'name':'机种属性1','value':'机种属性1url'}]}

    }

    return render(request,'index.html',message,status=200)

def uploda_data(request):
    message = ResponseMessage
    files = request.FILES.getlist("forecastfile")
    if files == None or len(files) <= 0:
        message.message = '不能上传空文件'
        return render_json(message)

