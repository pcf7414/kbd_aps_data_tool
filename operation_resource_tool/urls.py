from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^or/coverter/$', views.init_data, name='init_data'),
    url(r'^or/upload/$', views.uploda_data, name='upload_data'),
]
