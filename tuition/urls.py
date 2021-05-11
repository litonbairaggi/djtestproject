from django.urls import path
from .views import contact, postview

urlpatterns = [
    #path('contact/', views.contact, name='contact'),
    path('contact/',contact,name="contact"),
    path('posts/',postview,name="posts"),
]