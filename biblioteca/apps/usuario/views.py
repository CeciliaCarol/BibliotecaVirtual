from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_backends
from .forms import RegistroForm
from .forms import LoginForm
from .models import Usuario


def registrar_usuario(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Define o backend de autenticação
            backend = get_backends()[0]  # Pega o primeiro backend configurado
            user.backend = f"{backend.__module__}.{backend.__class__.__name__}"

            login(request, user)
            return redirect("usuario:login")  # Redireciona após registro
    else:
        form = RegistroForm()
    
    return render(request, "usuario/register.html", {"form": form})

def login_usuario(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            cpf = form.cleaned_data.get("cpf")
            password = form.cleaned_data.get("password")

            user = authenticate(request, cpf=cpf, password=password)
            if user is not None:
                login(request, user)
                return redirect("listar_livros")
            else:
                form.add_error(None, "CPF ou senha incorretos.")
    
    else:
        form = LoginForm()

    return render(request, "usuario/login.html", {"form": form})


def welcome(request):
    return render(request, "usuario/welcome.html")