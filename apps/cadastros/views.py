from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

# class IndexView(TemplateView):
#     template_name = 'index.html'


# from django.shortcuts import render

# def index(resquest):
#     return render(resquest, 'index.html')
