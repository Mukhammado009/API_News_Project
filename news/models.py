from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE_CHOICES= (
        ('A', 'admin'),
        ('M', 'author'),
    )
    role = models.CharField(max_length=200, choices=ROLE_CHOICES)
   

class Category(models.Model):
    name = models.CharField(max_length=255)
    

class News(models.Model):
    tittle = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField()
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True)
    auth = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)


class Comment(models.Model):
    news = models.ForeignKey(News,on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class Save(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    news = models.ForeignKey(News, on_delete=models.CASCADE)