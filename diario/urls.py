from django.urls import path
from . import views

app_name = 'diario'

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_usuario, name='login'),
    path('entrada/', views.criar_entrada, name='entrada_diario'),
    path('entradas/', views.exibir_entradas, name='exibir_entradas'),
    path("editar/<int:entrada_id>/", views.editar_entrada, name="editar_entrada"),
    path("excluir/<int:entrada_id>/", views.excluir_entrada, name="excluir_entrada"),
]
