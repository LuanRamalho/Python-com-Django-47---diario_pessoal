from django.db import models
from django.contrib.auth.models import User

# Modelo para as entradas do diário
class Entrada(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relaciona com o usuário
    data = models.DateTimeField(auto_now_add=True)  # Alterado para DateTimeField para armazenar data e hora
    texto = models.TextField()  # Texto da entrada

    def __str__(self):
        return f"Entrada de {self.user.username} em {self.data.strftime('%d/%m/%Y %H:%M')}"
