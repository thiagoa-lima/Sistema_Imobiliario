from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

class SobreView(TemplateView):
    template_name = 'sobre.html'

class BootView(TemplateView):
    template_name = 'boot.html'

class BootView(TemplateView):
    template_name = 'base.html'

class ClientesView(TemplateView):
    template_name = 'cadastros/clientes.html'

# class IndexView(TemplateView):
#     template_name = 'index.html'


# from django.shortcuts import render

# def index(resquest):
#     return render(resquest, 'index.html')
