from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, TemplateView
from sorteio.models import Pessoa, Sorteio

class CreatePessoaView(CreateView):
    model = Pessoa
    fields = ['nome', 'email', 'telefone']
    template_name = 'cadastrar_usuario.html'

class ListPessoas(ListView):
    model = Pessoa
    queryset = Pessoa.objects.filter(old=False)
    template_name = 'lista_sorteios.html'

class CadastroSucesso(DetailView):
    model = Pessoa
    template_name = 'cadastro_sucesso.html'

class Index(TemplateView):
    template_name = 'lista_sorteios.html'

class Sorteio(DetailView):
    model = Sorteio
    template_name = 'sorteio.html'

def participar_sorteio_pre(request, sorteio_id):
    return render(request, 'participar.html')

def participar_sorteio(request, user_id, sorteio_id):
    try:
        sorteio = Sorteio.objects.get(pk=sorteio_id)
        user = Pessoa.objects.get(pk=user_id)
        sorteio.inscritos.add(user)
    except Exception:
        return render(request, 'participando.html', {'success': False})
    return render(request, 'participando.html', {'success': True})
