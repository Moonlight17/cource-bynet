from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('files/', views.parsingFile, name='parsingFile'),
    path('participants/', views.ParticipantsList, name='ParticipantsList'),
    re_path(r'^aggregate/(?P<from_date>\d{2}-\d{2}-\d{4})/(?P<to_date>\d{2}-\d{2}-\d{4})/$', views.my_date_view, name='my_date')
]
