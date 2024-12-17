from django.db import models

class Orçamento(models.Model):
    codigo_orcamento = models.CharField(max_length=20, unique=True)
    nome_cliente = models.CharField(max_length=100)
    telefone_cliente = models.CharField(max_length=15)
    observacoes = models.TextField(blank=True, null=True)
    preco_final = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    data_entrada = models.DateTimeField(auto_now_add=True)
    data_saida = models.DateTimeField(null=True, blank=True)
    STATUS_CHOICES = [
        ('em_reparo', 'Em Reparo'),
        ('aguardando_pagamento', 'Aguardando Pagamento'),
        ('retirada', 'Retirada'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='em_reparo')

    def __str__(self):
        return f"{self.codigo_orcamento} - {self.nome_cliente}"

    class Meta:
        ordering = ['data_entrada']
