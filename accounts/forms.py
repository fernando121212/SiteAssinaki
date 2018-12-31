from django import forms
from django.db import models
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User


class Email(forms.Form):
    email = forms.EmailField(label='Email', max_length=150)
    email.widget.attrs.update({'class': 'form-control'})
    def enviar_email(self):
        subject = 'Seja bem vindo a nosso site'
        message = 'clique no link para criar sua conta https://assinaki.herokuapp.com/accounts/cadastro. '
        email_from = settings.EMAIL_HOST_USER
        email = ['fernandoti@live.com']
        send_mail(subject, message, email_from,email)



class LoginForm(forms.Form):

    username = forms.CharField(label=("Usuário"), strip=False, widget=forms.TextInput)
    username.widget.attrs.update({'class': 'form-control'})

    password = forms.CharField(label=("Senha"), strip=False, widget=forms.PasswordInput)
    password.widget.attrs.update({'class': 'form-control'})



class Cadastro(UserCreationForm):


    name_cliente = forms.CharField(label='Nome do cliente', max_length=150)
    name_cliente.widget.attrs.update({'class': 'form-control'})

    cliente_sobrenome = forms.CharField(label='Sobrenome', max_length=150)
    cliente_sobrenome.widget.attrs.update({'class': 'form-control'})

    username = forms.CharField(label=("Usuário"), strip=False, widget=forms.TextInput)
    username.widget.attrs.update({'class': 'form-control'})

    password1 = forms.CharField(label=("Senha"), strip=False, widget=forms.PasswordInput)
    password1.widget.attrs.update({'class': 'form-control'})

    password2 = forms.CharField(label=('Confirmação de senha'),strip=False, widget=forms.PasswordInput)
    password2.widget.attrs.update({'class': 'form-control'})

    cliente_data_nascimento = forms.CharField(label='Data de nascimento',widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    cliente_data_nascimento.widget.attrs.update({'class': 'form-control'})




    SOLTEIRA = 'SLT'
    CASADA = 'CSD'
    SEPARADA = 'SPD'
    DIVORCIADA = 'DVD'
    VIUVA = 'VUV'
    UNIAO_ESTAVEL = 'UET'


    REGIME = (
        (SOLTEIRA, 'Solteira(o)'),
        (CASADA, 'Casada(o)'),
        (DIVORCIADA, 'Divorciada(o)'),
        (SEPARADA, 'Separada'),
        (VIUVA, 'Viúva(o)'),
        (UNIAO_ESTAVEL, 'União estável'),
    )

    cliente_estado_civil = forms.ChoiceField(label='Estado civil', choices=REGIME)
    cliente_estado_civil.widget.attrs.update({'class': 'form-control'})

    cliente_email = forms.EmailField(label='Email', max_length=150)
    cliente_email.widget.attrs.update({'class': 'form-control'})

    def clean_email(self):
        cliente_email = self.cleaned_data['cliente_email']
        if User.objects.filter(cliente_email=cliente_email).exists():
            raise forms.ValidationError("Já existe usuário com este E-mail")
        return cliente_email


    def save(self, commit=True):
        user = super(Cadastro,self).save(commit=False)
        user.cliente_email = self.cleaned_data['cliente_email']
        if commit:
            user.save()
        return user

    cliente_phone_fixo = forms.CharField(label='Telefone fixo', max_length=10,widget=forms.TextInput(attrs={'class': 'text span8',
            'placeholder': '(DDD) 0000-0000', 'mask': 'fone'}))
    cliente_phone_fixo.widget.attrs.update({'class': 'form-control'})

    cliente_cel_phone = forms.CharField(label='Celular', max_length=11,widget=forms.TextInput(attrs={'class': 'text span8',
            'placeholder': '(DDD) 00000-000', 'mask': 'fone'}))
    cliente_cel_phone.widget.attrs.update({'class': 'form-control'})


    cliente_cpf = forms.CharField(label='CPF', max_length=11,widget=forms.TextInput(attrs={'class': 'text span8',
            'placeholder': '000.000.000-00', 'mask': 'fone'}))
    cliente_cpf.widget.attrs.update({'class': 'form-control'})

    BRASIL = 'BR'
    ARGENTINA = 'AR'
    PAISES = (
        (BRASIL, 'Brasil'),
        (ARGENTINA, 'Argentina'),
    )

    name_pais = forms.ChoiceField(label='Nome do país', choices=PAISES)
    name_pais.widget.attrs.update({'class' : 'form-control'})

    ACRE = 'AC'
    BAHIA = 'BA'

    ESTADOS = (
        (ACRE, 'Acre'),
        (BAHIA, 'Bahia'),
    )

    name_uf = forms.ChoiceField(label='Nome do  estado', choices=ESTADOS)
    name_uf.widget.attrs.update({'class': 'form-control'})

    rua_cep = forms.CharField(label='CEP', max_length=8,widget=forms.TextInput(attrs={'class': 'text span8',
            'placeholder': '00000-000', 'mask': 'cep'}))
    rua_cep.widget.attrs.update({'class': 'form-control'})

    RIO_BRANCO = 'RBR'
    CRUZEIRO_DO_SUL = 'CZS'
    SALVADOR = 'SSA'

    CIDADES = (
        (CRUZEIRO_DO_SUL, 'Cruzeiro do Sul'),
        (RIO_BRANCO, 'Rio Branco'),
        (SALVADOR, 'Salvador'),
    )

    name_cidade = forms.ChoiceField(label='Nome da cidade', choices=CIDADES)
    name_cidade.widget.attrs.update({'class': 'form-control'})

    name_bairro = forms.CharField(label='Nome do bairro', max_length=150)
    name_bairro.widget.attrs.update({'class': 'form-control'})

    name_rua = forms.CharField(label='Nome da rua', max_length=150)
    name_rua.widget.attrs.update({'class': 'form-control'})

    rua_numero = forms.CharField(label='Número', max_length=10)
    rua_numero.widget.attrs.update({'class': 'form-control'})

    rua_complemento = forms.CharField(label='Complemento', max_length=150)
    rua_complemento.widget.attrs.update({'class': 'form-control'})




    #     name_pj = forms.CharField(label='Nome', max_length=150)
    #     pj_razao_social = forms.CharField(label='Razão social', max_length=150)
    #     pj_cnpj = forms.CharField(label='CNPJ', max_length=14)
    #     pj_insc_estadual = forms.CharField(label='Inscrição estadul', max_length=20)
    #
#
#     name_cartao = forms.CharField(label='Cartão', max_length=150)
#     cartao_numero = forms.CharField(label='Número', max_length=50)
#     cartao_data = forms.DateField(label='Vencimento em')
#     cartao_security_cod = forms.CharField(label='Código de segurança', max_length=10)
#     cartao_password = forms.CharField(label='Senha', max_length=150)
#

