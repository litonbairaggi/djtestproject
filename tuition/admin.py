from django.contrib import admin

# Register your models here.

from . models import Contact, Post

admin.site.register(Contact)
admin.site.register(Post)
