from django import forms
from .models import Orçamento

class OrcamentoForm(forms.ModelForm):
    class Meta:
        model = Orçamento
        fields = ['codigo_orcamento', 'nome_cliente', 'telefone_cliente', 'observacoes', 'preco_final', 'status']
