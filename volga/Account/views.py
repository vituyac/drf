from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from .models import User
from .serializers import UserSerializer
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter, OpenApiResponse
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser, FormParser

@extend_schema(
    summary="Регистрация пользователя",
    description="Создаёт нового пользователя",
    request=UserSerializer
)
class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

@extend_schema(
    summary="Получение данных пользователя",
    description="Получение данных пользователя"
)
class UserMeAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
    
@extend_schema(
    summary="Обновление данных пользователя",
    description="Обновление данных пользователя"
)
class UserUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    http_method_names = ['put']
    
    def get_object(self):
        return self.request.user

@extend_schema(
    summary="Авторизация пользователя",
    description="Получение access и refresh токенов"
)
class TokenObtainPair(TokenObtainPairView):
    pass

class UsersAPIListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000

@extend_schema_view(
    list=extend_schema(
        summary="Список пользователей",
        description="Возвращает список всех пользователей",
        parameters=[
            OpenApiParameter(
                name='page_size',  
                description='Кол-во объектов на странице',
                required=False,
                type=int
            ),
            OpenApiParameter(
                name='page',  
                description='Номер страницы',
                required=False,
                type=int
            )
        ]
    ),
    retrieve=extend_schema(
        summary="Получение данных пользователя",
        description="Возвращает информацию о конкретном пользователе по ID",
    ),
    create=extend_schema(
        summary="Регистрация пользователя",
        description="Создаёт нового пользователя",
        request=UserSerializer,
    ),
    update=extend_schema(
        summary="Обновление данных пользователя",
        description="Обновляет данные существующего пользователя",
        request=UserSerializer,
    ),
    destroy=extend_schema(
        summary="Удаление пользователя",
        description="Удаляет существующего пользователя по ID",
    ),
)
class AdminViewSet(mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                mixins.ListModelMixin,
                GenericViewSet):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UsersAPIListPagination
    http_method_names = ['get', 'post', 'put', 'delete']
