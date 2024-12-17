from django.db import models

# Create your models here.

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
    
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Book(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='livros/')
    preco = models.FloatField()
    ano = models.IntegerField(default=2000)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, default=1)
    categoria = models.ManyToManyField(Categoria)
    def __str__(self):
        return self.nome
