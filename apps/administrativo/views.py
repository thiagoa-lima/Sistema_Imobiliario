from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView # usada para cadastros
from .models import Painel_administrativo
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Painel_Administrativo_View(LoginRequiredMixin, UpdateView):
    model = Painel_administrativo
    fields = '__all__'
    template_name = 'administrativo/painel.html'

    def get_success_url(self) -> str:
        return reverse_lazy('painel-administrativo', kwargs={'pk': 1})

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Painel Administrativo"
        context['botao'] = "Salvar"
        
        return context

