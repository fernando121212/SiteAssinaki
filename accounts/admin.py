from django.contrib import admin
from .models import Cliente, Pessoa_juridica, Login

# Register your models here.
@admin.register(Cliente)
class Cliente_admin(admin.ModelAdmin):
    list_display = ['name', 'slug','cliente_sobrnome','cliente_data_nascimento','cliente_estado_civil','cliente_email','cliente_phone_fixo','cliente_cel_phone','cliente_cpf','rua', 'created', 'modified']
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
