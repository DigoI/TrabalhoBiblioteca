from django.db import models

# Create your models here.
class Book(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='livros/')
    preco = models.FloatField()