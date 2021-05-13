from django.urls import path
from .views import contact, postview, postcreate, subview, ContactView
from .froms import ContactFormtwo


urlpatterns = [
    #path('contact/', views.contact, name='contact'),
    #path('contact/',contact,name="contact"),
    path('contact/',ContactView.as_view(),name="contact"),
    # path('contact2/',ContactView.as_view(form_class=ContactFormtwo, template_name="contact2.html"),name="contact2"),
    path('posts/',postview,name="posts"),
    path('subjects/',subview,name="subjects"),
    path('create/',postcreate,name="create"),
]