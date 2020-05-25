from django.shortcuts import render

# Create your views here.

def listar_tarefas(req):
    nome_tarefa = "Assitir a semana Python e Django da TreinaWeb"
    return render(req, 'tarefas/listar_tarefas.html', {"nome_tarefa": nome_tarefa})