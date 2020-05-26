from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def cadastrar_usuario(req):
    if req.method == "POST":
        form_usuario = UserCreationForm(req.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('listar_tarefas')
    else:
        form_usuario = UserCreationForm()

    return render(req, 'usuarios/form_usuario.html', {'form_usuario': form_usuario})

def logar_usuario(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        usuario = authenticate(req, username=username, password=password)
        if usuario is not None:
            login(req, usuario)
            return redirect('listar_tarefas')
        else:
            messages.error(req, 'As credenciais estão incorretas')
            return redirect('logar_usuario')
    else:
        form_login = AuthenticationForm()
    return render(req, 'usuarios/login.html', {'form_login': form_login})

def deslogar_usuario(req):
    logout(req)
    return redirect('logar_usuario')