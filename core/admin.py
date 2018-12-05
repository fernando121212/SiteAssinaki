from django.contrib import admin
from .models import Pais, Uf, Cidade, Bairro, Rua

@admin.register(Pais)
class Pais_admin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Uf)
class Uf_admin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'pais']
    search_fields = ['name', 'slug', 'pais__name']
    list_display_links = ['pais']
    list_select_related = ['pais']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Cidade)
class Cidade_admin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'uf']
    search_fields = ['name', 'slug', 'uf__name']
    list_display_links = ['uf']
    list_select_related = ['uf']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Bairro)
class Bairro_admin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'cidade']
    search_fields = ['name', 'slug', 'cidade__name']
    list_display_links = ['cidade']
    list_select_related = ['cidade']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Rua)
class Rua_admin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'rua_numero', 'rua_complemento', 'rua_cep', 'bairro', 'created', 'modified']
    search_fields = ['name', 'slug', 'bairro__name']
    list_filter = ['created', 'modified']
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ['bairro']
    list_select_related = ['bairro']



