from django.db import models
from django.utils.timezone import now


# Create your models here.

class Contact(models.Model):
    name= models.CharField(max_length=100, blank= False)
    phone= models.CharField(max_length=17, unique=True, blank= False)
    content = models.TextField(max_length=700,blank=False)
    
    #model method
    def __str__(self):
        return self.name

class Post(models.Model):
    CATEGORY = (
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    )
    title = models.CharField(max_length=100, blank= False)
    slug = models.CharField(max_length=100, default=title)    
    email = models.EmailField(max_length=32, blank= False)    
    salary = models.FloatField(default=0) 
    details = models.TextField(max_length=200, blank= False)
    available = models.BooleanField()
    category = models.CharField(max_length=100, choices=CATEGORY)  
    image = models.ImageField(default='default.jpg', upload_to='tuition/images')
    created_at = models.DateTimeField(default=now)
