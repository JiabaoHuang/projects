from django.urls import path,re_path
from . import views

urlpatterns = [
    path('daily',views.daily_handler,name='daily'),
    path('weekly', views.weekly_handler, name='weekly')
]