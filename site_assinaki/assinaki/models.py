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

class Bairro(models.Model):
    bairro_nome = models.CharField('Nome do bairro', max_length=50)
    cidade = models.ForeignKey('Cidade', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.bairro_nome

    class Meta:
        verbose_name = 'Bairro'
        verbose_name_plural = "Bairros"

class Rua(models.Model):
    rua_nome = models.CharField('Nome da rua', max_length=150)
    rua_numero = models.CharField('Número', max_length=10)
    rua_complemento = models.CharField('Complemento', max_length=150)
    rua_cep = models.CharField('CEP', max_length=50)
    bairro = models.ForeignKey('Bairro', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.rua_nome

    class Meta:
        verbose_name = 'Rua'
        verbose_name_plural = "Ruas"


