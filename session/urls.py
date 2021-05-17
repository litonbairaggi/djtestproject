from django.urls import path
from .views import loginuser

app_name="session"
urlpatterns = [
    path('login/',loginuser,name="login"),
]