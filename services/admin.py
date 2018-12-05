from django.contrib import admin
from .models import Assinatura, Dados_cartao, Tipo_documento, Documento, PrecoAssinatura


# Register your models here.

@admin.register(PrecoAssinatura)
class PrecoAssinatura_admin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug']
    list_filter = ['created', 'modified']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Assinatura)
class Assinatura_admin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'cliente', 'created', 'modified']
    search_fields = ['name', 'slug', 'cliente__name']
    list_filter = ['created', 'modified']
    list_display_links = ['cliente']
    list_select_related = ['cliente']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Dados_cartao)
class Dados_cartao_admin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'cartao_numero', 'cartao_data', 'cartao_security_cod', 'cartao_password', 'pais', 'created', 'modified']
    search_fields = ['name', 'slug', 'pais__name']
    list_filter = ['created', 'modified']
    list_display_links = ['pais']
    list_select_related = ['pais']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tipo_documento)
class Tipo_documento_admin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug']
    list_filter = ['created', 'modified']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Documento)
class Documento_admin(admin.ModelAdmin):
    list_display = ['name', 'slug','documento_data','documento_quantidade_partes','tipo_documento', 'created', 'modified']
    search_fields = ['name', 'slug', 'tipo_documento__name']
    list_filter = ['created', 'modified']
    list_display_links = ['tipo_documento']
    list_select_related = ['tipo_documento']
    prepopulated_fields = {'slug': ('name',)}