from django.contrib import admin
from .models import Pais, Uf, Cidade, Bairro, Rua


# Register your models here.

@admin.register(Pais)
class Pais_admin(admin.ModelAdmin):
    list_display = ['pais_nome']

@admin.register(Uf)
class Uf_admin(admin.ModelAdmin):
    list_display = ['uf_nome', 'pais']
    list_display_links = ['pais']
    list_select_related = ['pais']

@admin.register(Cidade)
class Cidade_admin(admin.ModelAdmin):
    list_display = ['cidade_nome', 'uf']
    list_display_links = ['uf']
    list_select_related = ['uf']

@admin.register(Bairro)
class Bairro_admin(admin.ModelAdmin):
    list_display = ['bairro_nome', 'cidade']
    list_display_links = ['cidade']
    list_select_related = ['cidade']

@admin.register(Rua)
class Rua_admin(admin.ModelAdmin):
    list_display = ['rua_nome', 'rua_numero', 'rua_complemento', 'rua_cep', 'bairro']
    list_display_links = ['bairro']
    list_select_related = ['bairro']

