from django.shortcuts import render,redirect



def index(request):
    #return render(request, 'index.html')
    return redirect('converter')

def converter(request):
    context ={'files':{
        'product_attribute':[{'name':'a.xlsx','value':'data/a-uuid.a.xlsx'}],
        'item_project':[{'name':'a.xlsx','value':'data/a-uuid.a.xlsx'}]
    }}
    return render(request, 'converter.html',context=context)


def converter_upload(request):

    return redirect('converter')
