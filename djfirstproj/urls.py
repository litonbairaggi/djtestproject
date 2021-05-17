from django.contrib import admin
from django.urls import path, include
from .views import home, HomeView
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home, name="home"),
    path('',HomeView.as_view(), name="homeview"),
    #path('',TemplateView.as_view(template_name='home.html'), name="homeview"),
    path('tuition/', include('tuition.urls')),
    path('session/', include('session.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
