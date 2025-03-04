from django.db import models
from django.contrib.auth.models import User

# Modelo para as entradas do diário
class Entrada(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relaciona com o usuário
    data = models.DateField(auto_now_add=True)  # Data da entrada (automática)
    texto = models.TextField()  # Texto da entrada

    def __str__(self):
        return f"Entrada de {self.user.username} em {self.data.strftime('%d/%m/%Y')}"
