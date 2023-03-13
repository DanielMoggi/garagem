from django.db import models

# Create your models here.

class Marca(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(nax_length=50)
    

    def __str__(self):
        return self.nome.upper()

