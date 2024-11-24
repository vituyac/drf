from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter, OpenApiResponse
# Create your views here.

@extend_schema_view(
    post=extend_schema(
        summary="Регистрация пользователя",
        description="Создаёт нового пользователя",
        request=UserSerializer,
        responses={
            201: OpenApiResponse(response=UserSerializer, description="Пользователь успешно создан"),
            400: OpenApiResponse(description="Ошибки валидации")
        }
    ),
    patch=extend_schema(
        summary="Обновление данных пользователя",
        description="Обновляет данные существующего пользователя",
        request=UserSerializer,
        responses={
            200: OpenApiResponse(response=UserSerializer, description="Данные пользователя успешно обновлены"),
            400: OpenApiResponse(description="Ошибки валидации"),
            404: OpenApiResponse(description="Пользователь не найден")
        }
    )
)
class RegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    #http_method_names = ['get']
    # def post(self, request, *args, **kwargs):
    #     return super().post(request, *args, **kwargs)