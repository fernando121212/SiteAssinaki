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
        verbose_name_plural = 'Ruas'


class Cliente(models.Model):
    cliente_nome = models.CharField('Nome', max_length=150)
    cliente_sobrnome = models.CharField('Sobrnome', max_length=150)
    cliente_data_nascimento = models.DateField('Data')
    cliente_estado_civil = models.CharField('Estado civil', max_length=150)
    cliente_email = models.EmailField('Email', max_length=150)
    cliente_phone_fixo = models.CharField('Telefone fixo', max_length=50)
    cliente_cel_phone = models.CharField('Celular', max_length=50)
    cliente_cpf = models.CharField('CPF', max_length=11)
    rua = models.ForeignKey('Rua', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.Cliente_nome

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = "Clientes"

class Pessoa_juridica(models.Model):
    pj_nome = models.CharField('Nome', max_length=150)
    pj_razao_social = models.CharField('Razão social', max_length=150)
    pj_cnpj = models.CharField('CNPJ', max_length=14)
    pj_insc_estadual = models.CharField('Inscrição estadul', max_length=20)
    cliente = models.ForeignKey('Cliente', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.pj_nome

    class Meta:
        verbose_name = 'Pessoa juridica'
        verbose_name_plural = "Pessoas juridicas"

class Login(models.Model):
    login_username = models.CharField('Login', max_length=150)
    login_password = models.CharField('Password', max_length=150)
    cliente = models.ForeignKey('Cliente', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.login_username

    class Meta:
        verbose_name = 'Login'
        verbose_name_plural = "Logins"

class Assinatura(models.Model):
        assinatura_cod = models.CharField('Assinatura', max_length=11)
        cliente = models.ForeignKey('Cliente', on_delete=models.DO_NOTHING)

        def __str__(self):
            return self.assinatura_cod

        class Meta:
            verbose_name = 'Assinatura'
            verbose_name_plural = "Assinaturas"

class Dados_cartao(models.Model):
    cartao_nome = models.CharField('Cartão', max_length=150)
    cartao_numero = models.CharField('Número', max_length=50)
    cartao_data = models.DateField('Data')
    cartao_security_cod = models.CharField('Código', max_length=10)
    cartao_password = models.CharField('Password', max_length=150)
    pais = models.ForeignKey('Pais', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.cartao_nome

    class Meta:
        verbose_name = 'Dados_cartao'
        verbose_name_plural = "Dados_cartao"