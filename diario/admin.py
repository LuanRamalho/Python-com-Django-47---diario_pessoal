from django.contrib import admin
from .models import Entrada

@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    list_display = ('user', 'data')  # Exibe essas colunas no painel
    search_fields = ('user__username', 'data')  # Permite buscar pelo nome do usuário ou data
    list_filter = ('data',)  # Adiciona um filtro por data

