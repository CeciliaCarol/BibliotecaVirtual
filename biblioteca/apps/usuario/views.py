from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistroForm

def registrar_usuario(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")  # Redireciona após registro
    else:
        form = RegistroForm()
    
    return render(request, "usuario/register.html", {"form": form})