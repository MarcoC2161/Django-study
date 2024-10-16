from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index), #views파일에서 index함수를 가져오라는 의미
    path('menu/<str:food>/', views.food_detail),
]