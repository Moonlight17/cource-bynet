from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('files/', views.parsingFile, name='parsingFile'),
    re_path(r'^aggregate/(?P<from_date>\d{4}-\d{2}-\d{2})/(?P<to_date>\d{4}-\d{2}-\d{2})/$', views.my_date_view, name='my_date')
]
