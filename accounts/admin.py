from django.contrib import admin
from . models import Cliente, Pessoa_juridica, Login

# Register your models here.
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
