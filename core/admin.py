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
    list_display = ['name', 'slug', 'texto', 'created', 'modified'] # name é o título; texto é o conteúdo
    search_fields = ['name', 'slug']
    list_filter = ['created', 'modified']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(PrecoAssinatura)
class PrecoAssinatura_admin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'modified'] # name é o Preço base
    search_fields = ['name', 'slug']
    list_filter = ['created', 'modified']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(StatusPagamento)
class StatusPagamento(admin.ModelAdmin):
    list_display = ['cliente', 'cartao', 'created', 'modified']
    search_fields = ['cliente__name', 'cartao__cartao_numero']
    list_display_links = ['cliente', 'cartao']
    list_filter = ['created', 'modified']


