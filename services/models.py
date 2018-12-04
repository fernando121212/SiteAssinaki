from django.db import models
from django.db.models import ForeignKey
from accounts.models import Cliente
from core.models import Pais

# Create your models here.

class Assinatura(models.Model):
        assinatura_cod = models.CharField('Assinatura', max_length=11)
        cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)

        def __str__(self):
            return self.assinatura_cod

        class Meta:
            verbose_name = 'Assinatura'
            verbose_name_plural = "Assinaturas"

class Dados_cartao(models.Model):
    cartao_nome = models.CharField('Cartão', max_length=150)
    cartao_numero = models.CharField('Número', max_length=50)
    cartao_data = models.DateField('Vencimento em')
    cartao_security_cod = models.CharField('Código de segurança', max_length=10)
    cartao_password = models.CharField('Senha', max_length=150)
    pais = models.ForeignKey(Pais, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.cartao_nome

    class Meta:
        verbose_name = 'Dados do cartao'
        verbose_name_plural = "Dados dos cartões"

class Tipo_documento(models.Model):
    nome_tipo_documento = models.CharField('Tipo de documento', max_length=50)


    def __str__(self):
        return self.nome_tipo_documento

    class Meta:
        verbose_name = 'Tipo de documento'
        verbose_name_plural = "Tipos de documentos"

class Documento(models.Model):
    documento_content = models.CharField("Documento", max_length=150)
    documento_data = models.DateField("Disponível até")
    documento_quantidade_partes = models.IntegerField('Quantas partes')
    tipo_documento = models.ForeignKey('Tipo_documento', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.documento_content

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = "Documentos"