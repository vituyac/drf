from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

class User(AbstractUser):
    #photo = models.ImageField(upload_to="users", blank=True, null=True, verbose_name='Фотография', default='users/none.jpg')
    #first_name = models.CharField(max_length=100)  
    #last_name = models.CharField(max_length=100)      

    def save(self, *args, **kwargs):
        if not self.is_superuser and not self.pk:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
