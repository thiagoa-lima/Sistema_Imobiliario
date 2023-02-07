from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView # usada basicamente para cadastros
from django.views.generic.list import ListView

from .models import Clientes, Imoveis
from django.urls import reverse_lazy

# ===================================================================================
# CREATE ('C' - CRUD)
# ===================================================================================

class ClientesCreate(CreateView):
    model = Clientes
    fields = ['cpf', 'nome', 'tipo_cliente', 'qualificacao',]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-clientes')

class ImoveisCreate(CreateView):
    model = Imoveis
    fields = ['proprietario', 'tipo', 'cep',]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

# ===================================================================================
# UPDATE ('U' - CRUD)
# ===================================================================================

class ClientesUpdate(UpdateView):
    model = Clientes
    fields = ['cpf', 'nome', 'tipo_cliente', 'qualificacao',]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-clientes')

class ImoveisUpdate(UpdateView):
    model = Imoveis
    fields = ['proprietario', 'tipo', 'cep',]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

# ===================================================================================
# DELETE ('D' - CRUD)
# ===================================================================================

class ClientesDelete(DeleteView):
    model = Clientes
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-clientes')

class ImoveisDelete(DeleteView):
    model = Imoveis
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')



# ===================================================================================
# LIST
# ===================================================================================

class ClientesList(ListView):
    model = Clientes
    template_name = 'cadastros/listas/clientes.html'




class IndexView(TemplateView):
    template_name = 'base.html'

class SobreView(TemplateView):
    template_name = 'sobre.html'

class BootView(TemplateView):
    template_name = 'boot.html'

class ClientesView(TemplateView):
    template_name = 'cadastro/form.html'
