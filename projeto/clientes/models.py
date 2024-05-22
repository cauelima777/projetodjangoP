
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(120)], null=True, blank=True)
    genero = models.CharField(max_length=10, choices=[('masculino', 'Masculino'), ('feminino', 'Feminino'), ('outro', 'Outro')], null=True, blank=True)
    email = models.EmailField(unique=True)
    data_cadastro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome
