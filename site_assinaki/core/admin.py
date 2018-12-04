from django.contrib import admin
from site_assinaki.assinaki.models import Assinatura
from site_assinaki.assinaki.models import Cliente


class AsinaturaAdmin(admin.ModelAdmin):
    ass = Assinatura()
    cli = Cliente()
  #  ass.assinatura_cod


