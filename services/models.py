from django.db import models
from django.db.models import ForeignKey



class Assinatura(models.Model):
        name = models.CharField('Assinatura', max_length=11)
        slug = models.SlugField('Identificador', max_length=150)
        cliente = models.ForeignKey('accounts.Cliente', verbose_name = 'Cliente', on_delete=models.DO_NOTHING)
        preco_base = models.ForeignKey('core.PrecoAssinatura', verbose_name = 'Preço base', on_delete=models.DO_NOTHING)

        created = models.DateTimeField('Criado em', auto_now_add=True)
        modified = models.DateTimeField('Modificado em', auto_now=True)

        def __str__(self):
            return self.name

        class Meta:
            verbose_name = 'Assinatura'
            verbose_name_plural = "Assinaturas"


class Documento(models.Model):
    name = models.CharField("Documento", max_length=150)
    slug = models.SlugField('Identificador', max_length=150)
    documento_data = models.DateField("Disponível até")
    documento_quantidade_partes = models.IntegerField('Quantas partes')
    tipo_documento = models.ForeignKey('core.Tipo_documento', verbose_name = 'Tipo de documento', on_delete=models.DO_NOTHING)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = "Documentos"

class DocumentoAssinado(models.Model):
    name = models.CharField("Documento assinado", max_length=15)
    slug = models.SlugField('Identificador', max_length=15)
    cliente = models.ForeignKey('accounts.Cliente', verbose_name='Cliente', on_delete=models.DO_NOTHING)
    documento = models.ForeignKey('Documento', verbose_name = 'Documento', on_delete=models.DO_NOTHING)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Documento assinado'
        verbose_name_plural = "Documentos assinados"