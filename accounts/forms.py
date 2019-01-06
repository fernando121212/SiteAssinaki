import email

from django import forms
from django.db import models
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from pip._vendor.html5lib._ihatexml import normaliseCharList


class Email(forms.Form):
    email = forms.EmailField(label='Digite seu E-mail', max_length=150)
    email.widget.attrs.update({'class': 'form-control'})
    def enviarEmailCadastro(self):
        subject = 'Seja bem vindo a nosso site'
        mensagem1 = 'clique no link para criar sua conta https://assinaki.herokuapp.com/accounts/cadastro. '
        email_from = settings.EMAIL_HOST_USER
        email = ['fernandoti@live.com']
        send_mail(subject, mensagem1, email_from,email)
    def enviarEmailSenha(self):
        subject = 'Seja bem vindo a nosso site'
        mensagem2 = 'clique no link para criar sua conta https://assinaki.herokuapp.com/accounts/cadastro. '
        email_form = settings.EMAIL_HOST_USER
        email = ['fernandoti@live.com']
        send_mail(subject,mensagem2,email_form,email)




class LoginForm(forms.Form):

    username = forms.CharField(label=("Usuário"), strip=False, widget=forms.TextInput)
    username.widget.attrs.update({'class': 'form-control'})

    password = forms.CharField(label=("Senha"), strip=False, widget=forms.PasswordInput)
    password.widget.attrs.update({'class': 'form-control'})


class Cadastro(UserCreationForm):
    first_name = forms.CharField(label='Nome do cliente', max_length=150)
    first_name.widget.attrs.update({'class': 'form-control'})

    last_name = forms.CharField(label='Sobrenome', max_length=150)
    last_name.widget.attrs.update({'class': 'form-control'})

    username = forms.CharField(label=("Usuário"), strip=False, widget=forms.TextInput)
    username.widget.attrs.update({'class': 'form-control'})

    password1 = forms.CharField(label=("Senha"), strip=False, widget=forms.PasswordInput)
    password1.widget.attrs.update({'class': 'form-control'})

    password2 = forms.CharField(label=('Confirmação de senha'),strip=False, widget=forms.PasswordInput)
    password2.widget.attrs.update({'class': 'form-control'})

    cliente_data_nascimento = forms.CharField(label='Data de nascimento',widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    cliente_data_nascimento.widget.attrs.update({'class': 'form-control'})

    SLT = 'Solteira(o)'
    CSD = 'Casada(o)'
    SPD = 'Separada(o)'
    DVD = 'Divorciada(o)'
    VUV = 'Viuva(o)'
    UET = 'União estável'

    REGIME = (
        (SLT, 'Solteira(o)'),
        (CSD, 'Casada(o)'),
        (DVD, 'Divorciada(o)'),
        (SPD, 'Separada(o)'),
        (VUV, 'Viúva(o)'),
        (UET, 'União estável'),
    )

    cliente_estado_civil = forms.ChoiceField(label='Estado civil', choices=REGIME)
    cliente_estado_civil.widget.attrs.update({'class': 'form-control'})

    email = forms.EmailField(label='Email', max_length=150)
    email.widget.attrs.update({'class': 'form-control'})

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Já existe usuário com este E-mail")
        return email

    def save(self, commit=True):
        user = super(Cadastro,self).save(commit=False)
        user.email = self.cleaned_data['email']
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

    BR = 'Brasil'
    AR = 'Argentina'
    PAISES = (
        (BR, 'Brasil'),
        (AR, 'Argentina'),
    )

    name_pais = forms.ChoiceField(label='Nome do país', choices=PAISES)
    name_pais.widget.attrs.update({'class' : 'form-control'})

    AC = 'Acre'
    BA = 'Bahia'

    ESTADOS = (
        (AC, 'Acre'),
        (BA, 'Bahia'),
    )

    name_uf = forms.ChoiceField(label='Nome do  estado', choices=ESTADOS)
    name_uf.widget.attrs.update({'class': 'form-control'})

    rua_cep = forms.CharField(label='CEP', max_length=8,widget=forms.TextInput(attrs={'class': 'text span8',
            'placeholder': '00000-000', 'mask': 'cep'}))
    rua_cep.widget.attrs.update({'class': 'form-control'})

    RBR = 'Rio Branco'
    CZS = 'Cruzeiro do Sul'
    SSA = 'Salvador'

    CIDADES = (
        (CZS, 'Cruzeiro do Sul'),
        (RBR, 'Rio Branco'),
        (SSA, 'Salvador'),
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

