from django.shortcuts import render

from django.views.generic.list import ListView

from .models import Fin_Aluguel
from django.urls import reverse_lazy
from . import forms

# CONTROLE DE LOGIN e USÁRIOS
from django.contrib.auth.mixins import LoginRequiredMixin

class Fin_Aluguel_List(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Fin_Aluguel
    template_name = 'financeiro/aluguel/lista.html'