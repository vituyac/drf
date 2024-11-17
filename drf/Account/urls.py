from django.contrib import admin
from django.urls import path, re_path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    re_path(r'^Authentication/SignUp/?$', RegistrationAPIView.as_view()),
    re_path(r'^Authentication/SignIn/?$', TokenObtainPairView.as_view()),
    re_path(r'^Authentication/Refresh/?$', TokenRefreshView.as_view()),
]