from django.contrib import admin
from accounts.models import Cliente
from . models import Assinatura, Dados_cartao, Tipo_documento, Documento


# Register your models here.


@admin.register(Assinatura)
class Assinatura_admin(admin.ModelAdmin):
    list_display = ['assinatura_cod','cliente']
    list_display_links = ['cliente']
    list_select_related = ['cliente']

@admin.register(Dados_cartao)
class Dados_cartao_admin(admin.ModelAdmin):
    list_display = ['cartao_nome', 'cartao_numero', 'cartao_data', 'cartao_security_cod', 'cartao_password', 'pais']
    list_display_links = ['pais']
    list_select_related = ['pais']


@admin.register(Tipo_documento)
class Tipo_documento_admin(admin.ModelAdmin):
    list_display = ['nome_tipo_documento']


@admin.register(Documento)
class Documento_admin(admin.ModelAdmin):
    list_display = ['documento_content','documento_data','documento_quantidade_partes','tipo_documento']
    list_display_links = ['tipo_documento']
    list_select_related = ['tipo_documento']