from django.db import models
from django.conf import settings  # Importa as configurações do projeto

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    generos = models.CharField(max_length=200)
    paginas = models.IntegerField()
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 

    def __str__(self):
        return self.titulo
