from django.contrib import admin
from django.urls import path, include
from sick.views import *

app_name = 'sick'
urlpatterns = [
    path('sick/create', SickCreateView.as_view()),
    path('all/', SickListView.as_view()),
    path('sick/detail/<int:pk>', SickDetailView.as_view())

]