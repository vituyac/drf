from django.db import models

class Book(models.model):
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
    