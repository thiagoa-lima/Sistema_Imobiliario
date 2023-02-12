from django import forms
from . import models


class AdministracaoForm(forms.ModelForm):
    class Meta:
        model = models.Administracao
        fields = '__all__'
        widgets = {
            "proprietario": forms.Select(attrs={'class': 'select2 form-control', 'data-placeholder': 'Selecione um proprietário', 'style': 'width: 100%'})            
        }

class AlugueloForm(forms.ModelForm):
    class Meta:
        model = models.Aluguel
        fields = '__all__'
        widgets = {
            "proprietario": forms.Select(attrs={'class': 'select2 form-control', 'data-placeholder': 'Selecione um proprietário', 'style': 'width: 100%'}),
            "locatario": forms.Select(attrs={'class': 'select2 form-control', 'data-placeholder': 'Selecione um locatário', 'style': 'width: 100%'}),

        }
     