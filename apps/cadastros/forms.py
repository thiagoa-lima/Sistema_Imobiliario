from django import forms
from . import models


class ImoveisForm(forms.ModelForm):
    class Meta:
        model = models.Imoveis
        fields = '__all__'
        exclude = []
        widgets = {
            "proprietario": forms.Select(attrs={'class': 'select2 form-control', 'data-placeholder': 'Selecione um proprietário', 'style': 'width: 100%'})            
        }

class ClientesFormAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientesFormAdmin, self).__init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs['class'] = 'mask-cpf'
        self.fields['celular'].widget.attrs['class'] = 'mask-telefone'
        self.fields['telefone'].widget.attrs['class'] = 'mask-telefone'
        self.fields['telefone_conjuge'].widget.attrs['class'] = 'mask-telefone'
        self.fields['celular_conjuge'].widget.attrs['class'] = 'mask-telefone'
        self.fields['cpf_conjuge'].widget.attrs['class'] = 'mask-cpf'
        self.fields['cep'].widget.attrs['class'] = 'mask-cep'

        
class ImoveisFormAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ImoveisFormAdmin, self).__init__(*args, **kwargs)
        self.fields['cep'].widget.attrs['class'] = 'mask-cep'
