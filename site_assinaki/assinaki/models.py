from django.db import models

# Create your models here.
from django.db.models import ForeignKey


class Pais(models.Model):
    pais_nome = models.CharField(max_length=50)

class Uf(models.Model):
    uf_nome = models.CharField(max_length=50)
    pais = models.ForeignKey('Pais', on_delete=models.DO_NOTHING)

class Cidade(models.Model):
    cidade_nome = models.CharField(max_length=50)
    uf = models.ForeignKey('Uf', on_delete=models.DO_NOTHING)

