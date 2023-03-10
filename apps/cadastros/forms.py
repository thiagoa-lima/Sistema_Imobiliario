from django import forms
from . import models


class Saida_de_Chaves_Form(forms.ModelForm):
    class Meta:
        model = models.Saida_de_Chaves
        fields = "__all__"
        exclude = []
        widgets = {
            "imovel": forms.Select(attrs={'class': 'select2 form-control', 'data-placeholder': 'Selecione um imóvel', 'style': 'width: 100%'}),          
            "cliente": forms.Select(attrs={'class': 'select2 form-control', 'data-placeholder': 'Selecione um cliente', 'style': 'width: 100%'}),   
            "observacao": forms.Textarea(attrs={'placeholder': 'Observação', 'style': 'width: 100%', 'rows':2, 'cols':40}),
        }

class ImoveisForm(forms.ModelForm):
    class Meta:
        model = models.Imoveis
        fields = '__all__'
        exclude = []
        widgets = {
            "proprietario": forms.Select(attrs={'class': 'select2 form-control', 'data-placeholder': 'Selecione um proprietário', 'style': 'width: 100%'}),          
        }

class Clientes_PJ_Form(forms.ModelForm):
    class Meta:
        model = models.ClientePJ
        fields = '__all__'
        exclude = []
        widgets = {
            "responsavel_1": forms.Select(attrs={'class': 'select2 form-control', 'data-placeholder': 'Selecione um cliente', 'style': 'width: 100%'}),               
            "responsavel_2": forms.Select(attrs={'class': 'select2 form-control', 'data-placeholder': 'Selecione um cliente', 'style': 'width: 100%'}),
            "nome": forms.TextInput(attrs={'placeholder': 'Razão Social da empresa'}),
        }
    
class Clientes_PF_Form(forms.ModelForm):
    class Meta:
        model = models.ClientePF
        fields = '__all__'
        exclude = []
        widgets = {
            "responsavel_1": forms.Select(attrs={'class': 'select2 form-control', 'data-placeholder': 'Selecione um cliente', 'style': 'width: 100%'}),               
            "responsavel_2": forms.Select(attrs={'class': 'select2 form-control', 'data-placeholder': 'Selecione um cliente', 'style': 'width: 100%'}),
        }

    # função criada para incluir o verbose name
    def __init__(self, *args, **kwargs):
        super(Clientes_PF_Form, self).__init__(*args, **kwargs)
        self.fields['email'].label = "E-mail"
    

class ClientesFormAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientesFormAdmin, self).__init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs['class'] = 'mask-cpf'
        self.fields['telefone'].widget.attrs['class'] = 'mask-telefone'
        self.fields['telefone_conjuge'].widget.attrs['class'] = 'mask-telefone'
        self.fields['celular_conjuge'].widget.attrs['class'] = 'mask-telefone'
        self.fields['cpf_conjuge'].widget.attrs['class'] = 'mask-cpf'
        self.fields['cep'].widget.attrs['class'] = 'mask-cep'

        
class ImoveisFormAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ImoveisFormAdmin, self).__init__(*args, **kwargs)
        self.fields['cep'].widget.attrs['class'] = 'mask-cep'
