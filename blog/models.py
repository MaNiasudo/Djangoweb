from django.db import models

# Create your models here.

class Post(models.Model):
    #image
    title = models.CharField(max_length=255)
    content = models.TextField()
    #tage
    #category
    #author
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)

    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return f"{self.title} - {self.id}"