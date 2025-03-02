from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm
from django.contrib.auth.decorators import login_required

@login_required
def listar_livros(request):
    livros = Livro.objects.filter(usuario=request.user)
    return render(request, 'livros/listar.html', {'livros': livros})

@login_required
def adicionar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            livro = form.save(commit=False)
            livro.usuario = request.user
            livro.save()
            return redirect('listar_livros')
    else:
        form = LivroForm()
    return render(request, 'livros/form.html', {'form': form})

@login_required
def editar_livro(request, id):
    livro = get_object_or_404(Livro, id=id, usuario=request.user)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'livros/form.html', {'form': form})

@login_required
def excluir_livro(request, id):
    livro = get_object_or_404(Livro, id=id, usuario=request.user)
    if request.method == 'POST':
        livro.delete()
        return redirect('listar_livros')
    return render(request, 'livros/confirmar_exclusao.html', {'livro': livro})
