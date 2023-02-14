from django import forms
from . import models


class Fin_Aluguel_Form(forms.ModelForm):
    class Meta:
        model = models.Fin_Aluguel
        fields = '__all__'
        # widgets = {
        #     "proprietario": forms.Select(attrs={'class': 'select2 form-control', 'data-placeholder': 'Selecione um proprietário', 'style': 'width: 100%'})            
        # }
