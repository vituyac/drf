from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse
# Create your views here.

class RegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    
    @extend_schema(
        summary="Регистрация пользователя",
        description="Создаёт нового пользователя",
        request=UserSerializer,
        responses={
            201: OpenApiResponse(response=UserSerializer, description="Пользователь успешно создан"),
            400: OpenApiResponse(description="Ошибки валидации")
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)