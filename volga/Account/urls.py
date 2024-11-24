from django.urls import path, include
from rest_framework import routers
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'Account', AdminViewSet)

urlpatterns = [
    path('Account/SignUp', UserCreateAPIView.as_view()),
    path('Account/SignIn', TokenObtainPair.as_view()),
    path('Account/Me', UserMeAPIView.as_view()),
    path('Account/Update', UserUpdateAPIView.as_view()),
    
    path('Admin/', include(router.urls)),
    
    
    # path('Admin/Account/<int:pk>', UserCreateAPIView.as_view()),
    # path('Admin/Account', TokenObtainPair.as_view()),
    # path('Admin/Account/<int:pk>', UserMeAPIView.as_view()),
    # path('Admin/Account/<int:pk>', UserUpdateAPIView.as_view()),
]