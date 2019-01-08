import re
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.core import validators


class Pais(models.Model):

    BR = 'Brasil'
    AR = 'Argentina'
    PAISES = (
        (BR, 'Brasil'),
        (AR, 'Argentina'),
    )

    name = models.CharField('Nome do país',max_length=50, choices=PAISES, default=BR)
    slug = models.SlugField('Identificador', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = "Países"

class Uf(models.Model):
    AC = 'Acre'
    BA = 'Bahia'
    ESTADOS = (
        (AC, 'Acre'),
        (BA, 'Bahia'),
    )
    name = models.CharField('Nome do  estado', max_length=50, choices=ESTADOS, default=BA)
    slug = models.SlugField('Identificador', max_length=150)
    pais = models.ForeignKey('Pais', verbose_name = 'País', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

class Cidade(models.Model):

    RBR = 'Rio Branco'
    CZS = 'Cruzeiro do Sul'
    SSA = 'Salvador'

    CIDADES = (
        (CZS, 'Cruzeiro do Sul'),
        (RBR, 'Rio Branco'),
        (SSA, 'Salvador'),
    )

    name = models.CharField('Nome da cidade', max_length=50, choices=CIDADES, default=SSA)
    slug = models.SlugField('Identificador', max_length=150)
    uf = models.ForeignKey('Uf', verbose_name = 'Estado', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = "Cidades"

class Bairro(models.Model):
    name = models.CharField('Nome do bairro', max_length=50)
    slug = models.SlugField('Identificador', max_length=150)
    cidade = models.ForeignKey('Cidade', verbose_name = 'Cidade', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Bairro'
        verbose_name_plural = "Bairros"

class Rua(models.Model):
    name = models.CharField('Nome da rua', max_length=150)
    slug = models.SlugField('Identificador', max_length=150)
    rua_numero = models.CharField('Número', max_length=10)
    rua_complemento = models.CharField('Complemento', max_length=150)
    rua_cep = models.CharField('CEP', max_length=50)
    bairro = models.ForeignKey('Bairro', verbose_name = 'Bairro', on_delete=models.DO_NOTHING)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Rua'
        verbose_name_plural = 'Ruas'

class Cliente(models.Model):
    SLT = 'Solteira(o)'
    CSD = 'Casada(o)'
    SPD = 'Separada(o)'
    DVD = 'Divorciada(o)'
    VUV = 'Viuva(o)'
    UET = 'União estável'

    REGIME = (
        (SLT, 'Solteira(o)'),
        (CSD, 'Casada(o)'),
        (DVD, 'Divorciada(o)'),
        (SPD, 'Separada(o)'),
        (VUV, 'Viúva(o)'),
        (UET, 'União estável'),
    )

    first_name = models.CharField('Nome do cliente', max_length=150)
    slug = models.SlugField('Identificador', max_length=150)
    last_name = models.CharField('Sobrenome', max_length=150)
    cliente_data_nascimento = models.DateField('Data',blank=False)
    cliente_estado_civil = models.CharField('Estado civil', max_length=150, choices=REGIME, default=SLT)
    email = models.EmailField('Email', max_length=150)
    cliente_phone_fixo = models.CharField('Telefone fixo', max_length=50)
    cliente_cel_phone = models.CharField('Celular', max_length=50)
    cliente_cpf = models.CharField('CPF', max_length=11)
    rua = models.ForeignKey('Rua', verbose_name = 'Rua', on_delete=models.DO_NOTHING)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = "Clientes"

class Pessoa_juridica(models.Model):
    name = models.CharField('Nome', max_length=150)
    slug = models.SlugField('Identificador', max_length=150)
    pj_razao_social = models.CharField('Razão social', max_length=150)
    pj_cnpj = models.CharField('CNPJ', max_length=14)
    pj_insc_estadual = models.CharField('Inscrição estadul', max_length=20)
    cliente = models.ForeignKey('Cliente', verbose_name = 'Cliente', on_delete=models.DO_NOTHING)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Pessoa juridica'
        verbose_name_plural = "Pessoas juridicas"

class Dados_cartao(models.Model):
    bandeira = models.CharField('Bandeira do cartão', max_length=150)
    name = models.CharField('Nome completo', max_length=150)
    slug = models.SlugField('Identificador', max_length=150)
    cartao_numero = models.CharField('Número', max_length=50)
    cartao_data = models.DateField('Vencimento em')
    cartao_security_cod = models.CharField('Código de segurança', max_length=10)
    cartao_password = models.CharField('Senha', max_length=150)
    pais = models.ForeignKey('Pais', verbose_name = 'País', on_delete=models.DO_NOTHING)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Dados do cartao'
        verbose_name_plural = "Dados dos cartões"