from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^ExamReg/', views.index, name='index'),
    re_path(r'^register/', views.register, name='register'),
]