"""kbd_aps_data_tool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls import url
from django.conf.urls.static import static
import operation_resource_tool
from operation_resource_tool import views
from django.conf import settings

from filebrowser.sites import site

urlpatterns = [
#    path('admin/', admin.site.urls),

    path('filebrowser/', site.urls),
    path('',operation_resource_tool.views.index,name='index'),
    path('or/',include('operation_resource_tool.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
