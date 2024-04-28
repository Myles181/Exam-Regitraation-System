from django.urls import path
from . import views

urlpatterns = [
    path('examhome', views.addq, name='addq'),
    path('exam', views.exam, name='exam'),
    path('result', views.result, name='result'),
    path('logout', views.logout, name='logout'),
    path('exam', views.exam, name='exam'),
    path('comp',views.comp,name='comp'),
]