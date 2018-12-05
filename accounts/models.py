from django.db import models

class Cliente(models.Model):
    name = models.CharField('Nome do cliente', max_length=150)
    slug = models.SlugField('Identificador', max_length=150)
    cliente_sobrnome = models.CharField('Sobrnome', max_length=150)
    cliente_data_nascimento = models.DateField('Data')
    cliente_estado_civil = models.CharField('Estado civil', max_length=150)
    cliente_email = models.EmailField('Email', max_length=150)
    cliente_phone_fixo = models.CharField('Telefone fixo', max_length=50)
    cliente_cel_phone = models.CharField('Celular', max_length=50)
    cliente_cpf = models.CharField('CPF', max_length=11)
    rua = models.ForeignKey('core.Rua', verbose_name = 'Rua', on_delete=models.DO_NOTHING)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.name

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

class Login(models.Model):
    name = models.CharField('Login', max_length=150)
    slug = models.SlugField('Identificador', max_length=150)
    login_password = models.CharField('Password', max_length=150)
    cliente = models.ForeignKey('Cliente', verbose_name = 'Cliente', on_delete=models.DO_NOTHING)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Login'
        verbose_name_plural = "Logins"