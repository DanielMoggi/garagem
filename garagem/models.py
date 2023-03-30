from django.db import models

# Create your models here.

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50, null=True, blank=True)
    

    def __str__(self):
        return self.nome.upper()



class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    


class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    


class Cor(models.Model):
    descricao = models.CharField(max_length=100)
    
    def __str__(self):
        return self.descricao
       
    class Meta:
            verbose_name_plural = "Cores"
    


class Veiculo(models.Model):
    Modelo = models.CharField(max_length=50)
    Marca = models.ForeignKey(
        Marca, on_delete=models.PROTECT, related_name="veiculos"
    )
    Categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="veiculos"
    )
    Cor = models.ForeignKey(
        Cor, on_delete=models.PROTECT, related_name="veiculos"
    )
    Ano = models.IntegerField(
        default=0, null=True, blank=True
    )
    Preco = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, default=0
    )

    def __str__(self):
        return f"  {self.Modelo} {self.Marca} {self.Ano} {self.Cor}"
        
        
