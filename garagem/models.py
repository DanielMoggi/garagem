from django.db import models

# Create your models here.

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50)


    def __str__(self):
        return self.nome.upper()
    
class Categoria(models.Model):
    descrição = models.CharField(max_length=100)
 


    def __str__(self):
        return self.descrição
    

