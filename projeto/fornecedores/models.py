# customers/models.py

from django.db import models

class Fornecedor(models.Model):
    nome_empresa = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14, unique=True)  # Considerando CNPJ como string para facilitar a validação
    email_contato = models.EmailField()
    telefone = models.CharField(max_length=20)
    endereco = models.TextField()

    def __str__(self):
        return self.nome_empresa
