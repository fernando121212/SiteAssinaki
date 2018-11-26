from django.db import models

# Create your models here.
from django.db.models import ForeignKey


class Pais(models.Model):
    pais_nome = models.CharField('Nome do país',max_length=50)

    def __str__(self):
        return self.pais_nome

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = "Países"

class Uf(models.Model):
    uf_nome = models.CharField('Nome do  estado', max_length=50)
    pais = models.ForeignKey('Pais', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.uf_nome

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

class Cidade(models.Model):
    cidade_nome = models.CharField('Nome da cidade', max_length=50)
    uf = models.ForeignKey('Uf', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.cidade_nome

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = "Cidades"


