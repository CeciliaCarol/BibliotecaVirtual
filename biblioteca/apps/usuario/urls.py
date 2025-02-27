from django.urls import path
from .views import registrar_usuario

app_name = "usuario" 

urlpatterns = [
    path('register/', registrar_usuario, name='register'),
]