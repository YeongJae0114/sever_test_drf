from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField(max_length=300)
    emotion = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True) 
