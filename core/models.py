from django.db import models


# Create your models here.
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

class Release (models.Model):
    name = models.CharField('Título', max_length=250)
    slug = models.SlugField('Identificador', max_length=150)
    description = models.TextField('Descrição', blank=True)
    texto = models.TextField('Conteúdo')
    image = models.ImageField(upload_to='images', verbose_name='Imagem', null=True, blank=True)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Atualização'
        verbose_name_plural = "Atualizações"

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

class StatusPagamento(models.Model):
    cliente = models.ForeignKey('accounts.Cliente', verbose_name='Cliente', on_delete=models.DO_NOTHING)
    cartao = models.ForeignKey('accounts.Dados_cartao', verbose_name='4 últimos dígitos do cartão', on_delete=models.DO_NOTHING)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.cliente

    class Meta:
        verbose_name = 'Status do pagamento'
        verbose_name_plural = "Status dos pagamentos"