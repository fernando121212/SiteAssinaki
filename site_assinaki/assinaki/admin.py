from django.contrib import admin
from .models import Pais, Uf, Cidade


# Register your models here.

@admin.register(Pais, Uf, Cidade)
class AdminAssinaki(admin.ModelAdmin):
    pass