from django.shortcuts import render

def index(resquest):
    return render(resquest, 'index.html')
