from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    title = models.CharField(max_length=255)
    content = models.TextField()
    #tage
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)

    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return f"{self.title} - {self.id}"
    
