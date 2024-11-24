from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def get_by_natural_key(self, email):
        return self.get(**{self.model.USERNAME_FIELD: email})
    
class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True, verbose_name='active')
    is_superuser = models.BooleanField(default=False, verbose_name='superuser status')
    is_staff = models.BooleanField(default=False, verbose_name='staff status')
    file = models.FileField(
        upload_to="users/files",
        blank=True,              
        null=True,                
        verbose_name='Файл'
    )
    #photo = models.ImageField(upload_to="users", blank=True, null=True, verbose_name='Фотография', default='users/none.jpg')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    