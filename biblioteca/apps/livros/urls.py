from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_livros, name='listar_livros'),
    path('novo/', views.adicionar_livro, name='adicionar_livro'),
    path('editar/<int:id>/', views.editar_livro, name='editar_livro'),
    path('excluir/<int:id>/', views.excluir_livro, name='excluir_livro'),
]
