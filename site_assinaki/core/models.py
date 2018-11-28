from django.db import models


class Tipo_documento(models.Model):
    nome_tipo_documento = models.CharField('Tipo de documento', max_length=50)


    def __str__(self):
        return self.nome_tipo_documento

    class Meta:
        verbose_name = 'Tipo_documento'
        verbose_name_plural = "Tipo_documentos"