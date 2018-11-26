from django.contrib import admin
from .models import Pais

# Register your models here.
class AdminAssinaki(admin.ModelAdmin):
    list_display = ["pais_nome"]

class Meta:
    model = Pais

admin.site.register(Pais, AdminAssinaki)