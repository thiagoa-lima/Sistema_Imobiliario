from django.urls import path
from .views import IndexView, SobreView, BootView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('boot/', BootView.as_view(), name='boot'),
]