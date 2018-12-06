from django.contrib import admin
from .models import Tipo_documento, Release, PrecoAssinatura, StatusPagamento

@admin.register(Tipo_documento)
class Tipo_documento_admin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug']
    list_filter = ['created', 'modified']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Release)
class Release_admin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'texto', 'created', 'modified']
    search_fields = ['name', 'slug']
    list_filter = ['created', 'modified']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(PrecoAssinatura)
class PrecoAssinatura_admin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug']
    list_filter = ['created', 'modified']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(StatusPagamento)
class PrecoAssinatura_admin(admin.ModelAdmin):
    list_display = ['cliente', 'cartao', 'created', 'modified']
    search_fields = ['cliente', 'cartao']
    list_display_links = ['cliente', 'cartao']
    list_filter = ['created', 'modified']


