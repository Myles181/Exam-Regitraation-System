from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^adminhome/', views.adminhome, name='adminhome'),
    re_path(r'^addexam/', views.addexam, name='addexam'),
    re_path(r'^alogout/', views.alogout, name='alogout'),
    re_path(r'^adminprofile/', views.adminprofile, name='adminprofile'),
    re_path(r'^adminchangepassword/', views.adminchangepassword, name='adminchangepassword'),
    re_path(r'^addcourse/', views.addcourse, name='addcourse'),
    re_path(r'^accept/(?P<p1>\w+)/(?P<p2>\w+)/$', views.accept, name='accept'),

   # url(r'^accept/(?P<parameter>[\w-]+)', views.accept, name='accept'),
    re_path(r'^reject/(?P<p1>\w+)/(?P<p2>\w+)/$', views.reject, name='reject'),
]