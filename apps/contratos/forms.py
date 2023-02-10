from django import forms
from django_select2 import forms as s2forms

from . import models

# class ProprietarioWidget(s2forms.ModelSelect2MultipleWidget):
#     search_fields = [
#         "proprietario__icontains",        
#     ]

class AdministracaoForm(forms.ModelForm):
    class Meta:
        model = models.Administracao
        fields = '__all__'
        widgets = {
            "proprietario": forms.Select(attrs={'class': 'select2 form-control', 'data-placeholder': 'Selecione um proprietário', 'style': 'width: 100%'})            
        }
        