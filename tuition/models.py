from django.db import models
from django.utils.timezone import now
from PIL import Image
from django.utils.text import slugify
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User




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
    MEDIUM = (
        ('Bangla', 'Bangla'),
        ('English', 'English'),
        ('Hindi', 'Hindi'),
        ('Spanis', 'bangla'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100, blank= False)
    slug = models.CharField(max_length=100, default=title)    
    email = models.EmailField(max_length=32, blank= False)    
    salary = models.FloatField(default=0) 
    details = models.TextField(max_length=200, blank= False)
    available = models.BooleanField()
    category = models.CharField(max_length=100, choices=CATEGORY)  
    image = models.ImageField(default='default.jpg', upload_to='tuition/images')
    created_at = models.DateTimeField(default=now)
    medium=MultiSelectField(max_length=100, max_choices=4, choices=MEDIUM, default='Bangla')

    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        super(Post, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
