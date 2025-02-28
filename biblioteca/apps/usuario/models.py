from django.contrib.auth.models import AbstractUser,Group,Permission
from django.db import models

class Usuario(AbstractUser):
    cpf = models.CharField(max_length=14, unique=True)  # CPF é único
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "cpf"  # Define CPF como campo de login
    REQUIRED_FIELDS = ["username", "email"]  # Campos obrigatórios além do CPF

    groups = models.ManyToManyField(
        Group,
        related_name="usuario_groups",  # Nome alternativo para evitar conflito
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="usuario_permissions",  # Nome alternativo para evitar conflito
        blank=True
    )

    def __str__(self):
        return self.username
    

    