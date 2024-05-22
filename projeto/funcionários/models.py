# customers/models.py

from django.db import models

class Funcionario(models.Model):
    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True) 
    cargo = models.CharField(max_length=100)
    email_corporativo = models.EmailField(unique=True)
    data_admissao = models.DateField()

    def __str__(self):
        return self.nome_completo
