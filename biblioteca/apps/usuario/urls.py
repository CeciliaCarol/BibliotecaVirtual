from django.urls import path
from .views import registrar_usuario, login_usuario, welcome

app_name = "usuario" 

urlpatterns = [
    path('register/', registrar_usuario, name='register'),
    path('login/', login_usuario, name='login'),
    path('welcome/', welcome, name='welcome'),
]