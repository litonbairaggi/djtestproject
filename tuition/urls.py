from django.urls import path
from .views import contact, postview, postcreate, subview, ContactView, PostCreateView, PostListView, PostDetailView, PostEditView, PostDeleteView
from .froms import ContactFormtwo

app_name="tuition"
urlpatterns = [
    #path('contact/', views.contact, name='contact'),
    #path('contact/',contact,name="contact"),
    path('contact/',ContactView.as_view(),name="contact"),
    # path('contact2/',ContactView.as_view(form_class=ContactFormtwo, template_name="contact2.html"),name="contact2"),
    path('posts/',postview,name="posts"),
    path('postlist/',PostListView.as_view(),name="postlist"),
    path('postdetail/<int:pk>/',PostDetailView.as_view(),name="postdetail"),
    path('edit/<int:pk>/',PostEditView.as_view(),name="edit"),
    path('delete/<int:pk>/',PostDeleteView.as_view(),name="delete"),
    path('subjects/',subview,name="subjects"),
    # path('create/',postcreate,name="create"),
    path('create/',PostCreateView.as_view(),name="create"),
]