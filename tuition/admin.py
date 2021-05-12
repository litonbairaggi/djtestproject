from django.contrib import admin

# Register your models here.

from . models import Contact, Post, Subject, Class_in

admin.site.register(Contact)
admin.site.register(Post)
admin.site.register(Subject)
admin.site.register(Class_in)
