from django.contrib import admin
from .models import Assinatura, Documento, DocumentoAssinado


# Register your models here.

@admin.register(Assinatura)
class Assinatura_admin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'cliente', 'created', 'modified']
    search_fields = ['name', 'slug', 'cliente__name']
    list_filter = ['created', 'modified']
    list_display_links = ['cliente']
    list_select_related = ['cliente']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Documento)
class Documento_admin(admin.ModelAdmin):
    list_display = ['name', 'slug','documento_data','documento_quantidade_partes','tipo_documento', 'created', 'modified']
    search_fields = ['name', 'slug', 'tipo_documento__name']
    list_filter = ['created', 'modified']
    list_display_links = ['tipo_documento']
    list_select_related = ['tipo_documento']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(DocumentoAssinado)
class DocumentoAssinado_admin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'cliente', 'documento', 'created', 'modified']
    search_fields = ['name', 'slug', 'cliente__name', 'documento__name']
    list_filter = ['created', 'modified']
    list_display_links = ['cliente', 'documento']
    list_select_related = ['cliente','documento']
    prepopulated_fields = {'slug': ('name',)}
