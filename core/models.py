from django.db import models


# Create your models here.
class Pais(models.Model):
    name = models.CharField('Nome do país',max_length=50)
    slug = models.SlugField('Identificador', max_length=150)

    def __str__(self):
        return self.name

    # @models.permalink
    # def get_absolute_url(self):
    #     return ('pais:detalhe', (), {'slug': self.slug})

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = "Países"

class Uf(models.Model):
    name = models.CharField('Nome do  estado', max_length=50)
    slug = models.SlugField('Identificador', max_length=150)
    pais = models.ForeignKey('Pais', verbose_name = 'País', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

class Cidade(models.Model):
    name = models.CharField('Nome da cidade', max_length=50)
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

class Release (models.Model):
    name = models.CharField('Título', max_length=250)
    slug = models.SlugField('Identificador', max_length=150)
    texto = models.TextField('Conteúdo', blank=True)
    # upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
    # image_path = models.FilePathField(path="/media/", match='foo.*', recursive=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Atualização'
        verbose_name_plural = "Atualizações"
