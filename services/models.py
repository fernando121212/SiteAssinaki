from django.db import models
from django.db.models import ForeignKey

class PrecoAssinatura(models.Model):
        name = models.DecimalField('Preço base', decimal_places=2, max_digits=8)
        slug = models.SlugField('Identificador', max_length=150)

        created = models.DateTimeField('Criado em', auto_now_add=True)
        modified = models.DateTimeField('Modificado em', auto_now=True)

        def __str__(self):
            return self.name

        class Meta:
            verbose_name = 'Preço base'
            verbose_name_plural = "Preços bases"

class Assinatura(models.Model):
        name = models.CharField('Assinatura', max_length=11)
        slug = models.SlugField('Identificador', max_length=150)
        cliente = models.ForeignKey('accounts.Cliente', verbose_name = 'Cliente', on_delete=models.DO_NOTHING)
        preco_base = models.ForeignKey('PrecoAssinatura', verbose_name = 'Preço base', on_delete=models.DO_NOTHING)

        created = models.DateTimeField('Criado em', auto_now_add=True)
        modified = models.DateTimeField('Modificado em', auto_now=True)

        def __str__(self):
            return self.name

        class Meta:
            verbose_name = 'Assinatura'
            verbose_name_plural = "Assinaturas"

class Dados_cartao(models.Model):
    name = models.CharField('Cartão', max_length=150)
    slug = models.SlugField('Identificador', max_length=150)
    cartao_numero = models.CharField('Número', max_length=50)
    cartao_data = models.DateField('Vencimento em')
    cartao_security_cod = models.CharField('Código de segurança', max_length=10)
    cartao_password = models.CharField('Senha', max_length=150)
    pais = models.ForeignKey('core.Pais', verbose_name = 'País', on_delete=models.DO_NOTHING)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Dados do cartao'
        verbose_name_plural = "Dados dos cartões"

class Tipo_documento(models.Model):
    name = models.CharField('Tipo de documento', max_length=50)
    slug = models.SlugField('Identificador', max_length=150)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo de documento'
        verbose_name_plural = "Tipos de documentos"

class Documento(models.Model):
    name = models.CharField("Documento", max_length=150)
    slug = models.SlugField('Identificador', max_length=150)
    documento_data = models.DateField("Disponível até")
    documento_quantidade_partes = models.IntegerField('Quantas partes')
    tipo_documento = models.ForeignKey('Tipo_documento', verbose_name = 'Tipo de documento', on_delete=models.DO_NOTHING)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = "Documentos"