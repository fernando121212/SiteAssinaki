from django.contrib import admin
from .models import Pais, Uf, Cidade


# Register your models here.

@admin.register(Pais)
class Pais_admin(admin.ModelAdmin):
    list_display = ['pais_nome']

@admin.register(Uf)
class Uf_admin(admin.ModelAdmin):
    list_display = ['uf_nome']

@admin.register(Cidade)
class Cidade_admin(admin.ModelAdmin):
    list_display = ['cidade_nome']