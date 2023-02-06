from django.urls import path
from .views import IndexView, SobreView, BootView, ClientesView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('bootstrap/', BootView.as_view(), name='boot'),
    path('base/', BootView.as_view(), name='base'),
    path('clientes/', ClientesView.as_view(), name='cadastros-clientes'),
]