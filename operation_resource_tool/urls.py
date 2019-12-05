from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^converter/$', views.converter, name='converter'),
    url(r'^upload/$', views.converter_upload, name='upload'),
    url(r'^convert/$', views.convert, name='convert'),

]
