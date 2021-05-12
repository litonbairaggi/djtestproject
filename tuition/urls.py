from django.urls import path
from .views import contact, postview, postcreate, subview

urlpatterns = [
    #path('contact/', views.contact, name='contact'),
    path('contact/',contact,name="contact"),
    path('posts/',postview,name="posts"),
    path('subjects/',subview,name="subjects"),
    path('create/',postcreate,name="create"),
]