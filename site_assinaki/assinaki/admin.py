from django.contrib import admin
from .models import Pais, Uf, Cidade, Bairro, Rua, Cliente, Pessoa_juridica, Login, Assinatura, Dados_cartao


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

@admin.register(Cliente)
class Cliente_admin(admin.ModelAdmin):
    list_display = ['cliente_nome','cliente_sobrnome','cliente_data_nascimento','cliente_estado_civil','cliente_email','cliente_phone_fixo','cliente_cel_phone','cliente_cpf','rua']
    list_display_links = ['rua']
    list_select_related = ['rua']

@admin.register(Pessoa_juridica)
class Pessoa_admin(admin.ModelAdmin):
    list_display = ['pj_nome','pj_razao_social','pj_cnpj','pj_insc_estadual','cliente']
    list_display_links = ['cliente']
    list_select_related = ['cliente']

@admin.register(Login)
class Login_admin(admin.ModelAdmin):
    list_display = ['login_username','login_password','cliente']
    list_display_links = ['cliente']
    list_select_related = ['cliente']

@admin.register(Assinatura)
class Assinatura_admin(admin.ModelAdmin):
    list_display = ['assinatura_cod','cliente']
    list_display_links = ['cliente']
    list_select_related = ['cliente']

@admin.register(Dados_cartao)
class Dados_cartao(admin.ModelAdmin):
    list_display = ['cartao_nome','cartao_numero','cartao_data','cartao_security_cod','cartao_password','pais']
    list_display_links = ['pais']
    list_select_related = ['pais']
