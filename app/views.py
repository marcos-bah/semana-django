from django.shortcuts import render, redirect
from .forms import TarefaForm
from .entidades.tarefa import Tarefa
from .services import tarefa_services

# Create your views here.

def listar_tarefas(req):
    nome_tarefa = "Assitir a semana Python e Django da TreinaWeb"
    return render(req, 'tarefas/listar_tarefas.html', {"nome_tarefa": nome_tarefa})

def cadastrar_tarefa(req):
    if req.method == "POST":
        form_tarefa = TarefaForm(req.POST)
        if form_tarefa.is_valid():
            titulo = form_tarefa.cleaned_data["titulo"]
            descricao = form_tarefa.cleaned_data["descricao"]
            data_expiracao = form_tarefa.cleaned_data["data_expiracao"]
            prioridade = form_tarefa.cleaned_data["prioridade"]

            tarefa_nova = Tarefa(titulo=titulo, descricao=descricao, data_expiracao=data_expiracao, prioridade=prioridade)

            tarefa_services.cadastrar_tarefa(tarefa_nova)

            return redirect('listar_tarefas')
    else:
        form_tarefa = TarefaForm()
    return render(req, 'tarefas/form_tarefa.html', {"form_tarefa": form_tarefa})