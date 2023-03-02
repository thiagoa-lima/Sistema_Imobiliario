from django import forms
from . import models
from datetime import datetime


class AdministracaoForm(forms.ModelForm):
    class Meta:
        model = models.Administracao
        fields = '__all__'
        widgets = {
            "imovel": forms.Select(attrs={'class': 'select2 form-control', 'data-placeholder': 'Digite um endereço', 'style': 'width: 100%'})            
        }

class AluguelForm(forms.ModelForm):
    class Meta:
        model = models.Aluguel
        fields = '__all__'
        widgets = {
            "proprietario": forms.Select(attrs={'class': 'select2 form-control', 'data-placeholder': 'Selecione um proprietário', 'style': 'width: 100%'}),
            "locatario": forms.Select(attrs={'class': 'select2 form-control', 'data-placeholder': 'Selecione um locatário', 'style': 'width: 100%'}),
            "fiador": forms.Select(attrs={'class': 'select2 form-control', 'data-placeholder': 'Selecione um fiador', 'style': 'width: 100%'}),
            "observacao_garantia": forms.Textarea(attrs={'data-placeholder': 'Observação', 'style': 'width: 100%', 'rows':2, 'cols':40}), 
        }

class Baixa_de_Parcela_Aluguel_Form(forms.ModelForm):
    class Meta:
        model = models.Financeiro_do_Contrato
        fields = ['contrato', 'parcela', 'vencimento', 'vencimento_real', 'data_pagamento', 'valor_aluguel', 'multa', 'juros', 'valor_total', 'valor_pago', 'saldo_aluguel' ]

class Baixa_de_Repasse_Aluguel_Form(forms.ModelForm):
    class Meta:
        model = models.Financeiro_do_Contrato
        fields = ['contrato', 'parcela', 'vencimento_repasse', 'valor_repasse', 'valor_aluguel', 'comissao', 'data_repasse', 'valor_repassado', 'saldo_repasse']
