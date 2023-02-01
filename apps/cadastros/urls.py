from django.contrib import admin
from django.urls import path, include
from apps.cadastros.views import index

urlpatterns = [
    path('', index),
]