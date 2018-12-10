from django.contrib import admin
from .models import Cliente, Pessoa_juridica, Dados_cartao, Login, Pais, Uf, Cidade, Bairro, Rua

# Register your models here.

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


@admin.register(Cliente)
class Cliente_admin(admin.ModelAdmin):
    list_display = ['name', 'slug','cliente_sobrenome','cliente_data_nascimento','cliente_estado_civil','cliente_email','cliente_phone_fixo','cliente_cel_phone','cliente_cpf','rua', 'created', 'modified']
    search_fields = ['name', 'slug', 'rua__name']
    list_filter = ['created', 'modified']
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ['rua']
    list_select_related = ['rua']

@admin.register(Pessoa_juridica)
class Pessoa_admin(admin.ModelAdmin):
    list_display = ['name', 'slug','pj_razao_social','pj_cnpj','pj_insc_estadual','cliente', 'created', 'modified']
    search_fields = ['name', 'slug', 'cliente__name']
    list_filter = ['created', 'modified']
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ['cliente']
    list_select_related = ['cliente']

@admin.register(Login)
class Login_admin(admin.ModelAdmin):
    list_display = ['name', 'slug','login_password','cliente', 'created', 'modified']
    search_fields = ['name', 'slug', 'cliente__name']
    list_filter = ['created', 'modified']
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ['cliente']
    list_select_related = ['cliente']

@admin.register(Dados_cartao)
class Dados_cartao_admin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'cartao_numero', 'cartao_data', 'cartao_security_cod', 'cartao_password', 'pais', 'created', 'modified']
    search_fields = ['name', 'slug', 'pais__name']
    list_filter = ['created', 'modified']
    list_display_links = ['pais']
    list_select_related = ['pais']
    prepopulated_fields = {'slug': ('name',)}

