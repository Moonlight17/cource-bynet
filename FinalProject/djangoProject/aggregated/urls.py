from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('init/', views.add_data_by_default, name='add_data_by_default'),
    path('files/', views.parsing_file, name='parsing_file'),
    path('participants/', views.participants_list, name='participants_list'),
    re_path(r'^aggregate/(?P<from_date>\d{2}-\d{2}-\d{4})/(?P<to_date>\d{2}-\d{2}-\d{4})/$', views.my_date_view, name='my_date')
]
