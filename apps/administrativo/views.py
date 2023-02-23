from django.shortcuts import render
from django.views.generic.edit import UpdateView # usada para cadastros
from .models import Painel_administrativo
from django.urls import reverse_lazy

# Create your views here.

class Painel_Administrativo_View(UpdateView):
    model = Painel_administrativo
    fields = '__all__'
    template_name = 'administrativo.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Painel Administrativo"
        context['botao'] = "Salvar"
        
        return context

