from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('search/', BookSearch.as_view()),
    path('add/', BookAdd.as_view())
]