from django.shortcuts import render, redirect
from .forms import TarefaForm
from .entidades.tarefa import Tarefa
from .services import tarefa_services

# Create your views here.

def listar_tarefas(req):
    tarefas = tarefa_services.listar_tarefas()
    return render(req, 'tarefas/listar_tarefas.html', {"tarefas": tarefas})

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

def editar_tarefa(req, id):
    tarefa_bd = tarefa_services.listar_tarefa_id(id)
    form_tarefa = TarefaForm(req.POST or None, instance=tarefa_bd)
    if form_tarefa.is_valid():
        titulo = form_tarefa.cleaned_data["titulo"]
        descricao = form_tarefa.cleaned_data["descricao"]
        data_expiracao = form_tarefa.cleaned_data["data_expiracao"]
        prioridade = form_tarefa.cleaned_data["prioridade"]

        tarefa_nova = Tarefa(titulo=titulo, descricao=descricao, data_expiracao=data_expiracao, prioridade=prioridade)

        tarefa_services.editar_tarefa(tarefa_bd, tarefa_nova)
        return redirect('listar_tarefas')
    return render(req, 'tarefas/form_tarefa.html', {"form_tarefa": form_tarefa})

def remover_tarefa(req, id):
    tarefa_bd = tarefa_services.listar_tarefa_id(id)
    if req.method == 'POST':
        tarefa_services.remover_tarefa(tarefa_bd)
        return redirect('listar_tarefas')
    return render(req, 'tarefas/confirma_exclusao.html', {'tarefa': tarefa_bd})