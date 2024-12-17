from django.shortcuts import render, get_object_or_404, redirect
from .models import Orçamento
from .forms import OrcamentoForm

def listar_orcamentos(request):
    orcamentos = Orçamento.objects.all()
    return render(request, 'listar_orcamentos.html', {'orcamentos': orcamentos})

def adicionar_orcamento(request):
    if request.method == 'POST':
        form = OrcamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_orcamentos')
    else:
        form = OrcamentoForm()
    return render(request, 'adicionar_orcamento.html', {'form': form})

def editar_orcamento(request, codigo_orcamento):
    orcamento = get_object_or_404(Orçamento, codigo_orcamento=codigo_orcamento)
    if request.method == 'POST':
        form = OrcamentoForm(request.POST, instance=orcamento)
        if form.is_valid():
            form.save()
            return redirect('listar_orcamentos')
    else:
        form = OrcamentoForm(instance=orcamento)
    return render(request, 'editar_orcamento.html', {'form': form, 'orcamento': orcamento})

def alterar_status(request, codigo_orcamento):
    orcamento = get_object_or_404(Orçamento, codigo_orcamento=codigo_orcamento)
    if request.method == 'POST':
        novo_status = request.POST.get('status')
        orcamento.status = novo_status
        orcamento.save()
        return redirect('listar_orcamentos')
    return render(request, 'alterar_status.html', {'orcamento': orcamento})
