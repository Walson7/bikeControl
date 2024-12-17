from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_orcamentos, name='listar_orcamentos'),
    path('adicionar/', views.adicionar_orcamento, name='adicionar_orcamento'),
    path('editar/<str:codigo_orcamento>/', views.editar_orcamento, name='editar_orcamento'),
    path('alterar_status/<str:codigo_orcamento>/', views.alterar_status, name='alterar_status'),
]
