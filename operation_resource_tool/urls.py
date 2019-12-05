from django.conf.urls import url
from django.urls import path
from . import views
from django.conf.urls import url

# <<<<<<< HEAD
# urlpatterns = [
#     path('', views.index, name='index'),
#     url(r'^or/coverter/$', views.init_data, name='init_data'),
#     url(r'^or/upload/$', views.uploda_data, name='upload_data'),
# =======
urlpatterns=[
 url(r'^converter/$',views.converter, name='converter'),
 url(r'^upload/$', views.converter_upload,name='upload')

]
