from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^shome/', views.shome, name='shome'),
    re_path(r'^logout/', views.logout, name='logout'),
    re_path(r'^examregister/', views.examregister, name='examregister'),
    re_path(r'^mycourses/', views.mycourses, name='mycourses'),
    re_path(r'^hallticket/', views.hallticket, name='hallticket'),
    re_path(r'^profile/', views.profile, name='profile'),
    re_path(r'^password/', views.password, name='password'),
    re_path(r'^examht/(?P<parameter>[\w-]+)', views.examht, name='examht'),
    re_path(r'^pastexam/', views.pexam, name='pastexam'),
]