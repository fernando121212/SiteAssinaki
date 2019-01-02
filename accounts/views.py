from django.shortcuts import redirect, get_object_or_404
from .forms import Cadastro,LoginForm,Email
from .models import Cliente, Pais, Uf, Cidade, Bairro, Rua, Pessoa_juridica, Login, Dados_cartao
from django.contrib.auth import authenticate,login
from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

# @login_required
# def dashboard(request):
#     return render(request, 'contas/dashboard.html')

pais = Pais()

uf = Uf()
cidade = Cidade()
bairro = Bairro()
rua = Rua()
cliente = Cliente()
# pj = Pessoa_juridica()
# login = Login()
# cartao = Dados_cartao



def email_cadastro(request):
    tamplate_name = 'enviar_email_cadastro.html'
    context = {}
    if request.method == 'POST':
        form = Email(request.POST)
        if form.is_valid():

             context['is_valid'] = True
             form = Email()
             form.enviarEmailCadastro()

        return redirect('accounts:enviar_email_cadastro')

    else:
        form = Email()
        context['enviar_email_cadastro'] = form
    return render(request, tamplate_name, context)

def email_senha(request):
    tamplate_name = 'enviar_email_senha.html'
    context = {}
    if request.method == 'POST':
        form = Email(request.POST)
        if form.is_valid():

             context['is_valid'] = True
             form = Email()
             form.enviarEmailsenha()

        return redirect('accounts:enviar_email_senha')

    else:
        form = Email()
        context['enviar_email_senha'] = form
    return render(request, tamplate_name, context)


# def login(request):
#
#     tamplate_name = 'login.html'
#
#     if request.method == 'POST':
#         form_login = LoginCadastro(request.POST or None);
#
#         if form_login.is_valid():
#
#             form_data = form_login.cleaned_data
#
#             username = form_data.get('username')
#             login.username = username
#             password = form_data.get('password')
#             login.password = password
#             login.cliente = cliente
#             # login.save()
#             # return redirect('accounts:cadastro')
#
#     else:
#         form_login = LoginCadastro()
#
#
#     context = {
#         'title': 'login',
#         'form_login': form_login,
#
#
#     }
#     return render(request, tamplate_name, context)

def form_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                   password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)

                    return redirect('accounts:login')
                else:
                    return HttpResponse('Desabilitar account')
            else:
                return HttpResponse('Login Inválido')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form_login': form})


def cadastro(request):

    tamplate_name = "cadastro.html"


    if request.method == 'POST':
        form_cadastro = Cadastro(request.POST or None);

        if form_cadastro.is_valid():
            user = form_cadastro.save()
            user = authenticate(username = user.username, password=form_cadastro.cleaned_data['password1'])
            login(request,user)
            form_data = form_cadastro.cleaned_data

            name_pais = form_data.get('name_pais')
            pais.name = name_pais
            pais.save()

            name_uf = form_data.get('name_uf')
            uf.pais = pais
            uf.name = name_uf
            uf.save()

            rua_cep = form_data.get('rua_cep')
            rua.rua_cep = rua_cep

            name_cidade = form_data.get('name_cidade')
            cidade.uf = uf
            cidade.name = name_cidade
            cidade.save()

            name_bairro = form_data.get('name_bairro')
            bairro.cidade = cidade
            bairro.name = name_bairro
            bairro.save()

            name_rua = form_data.get('name_rua')
            rua.bairro = bairro
            rua.name = name_rua

            rua_numero = form_data.get('rua_numero')
            rua.rua_numero = rua_numero

            rua_complemento = form_data.get('rua_complemento')
            rua.rua_complemento = rua_complemento
            rua.save()


            cliente.rua = rua
            name_cliente = form_data.get('name_cliente' )
            cliente.name = name_cliente

            sobrenome = form_data.get('cliente_sobrenome')
            cliente.cliente_sobrenome = sobrenome

            data = form_data.get('cliente_data_nascimento')
            cliente.cliente_data_nascimento = data

            estado_civil = form_data.get('cliente_estado_civil')
            cliente.cliente_estado_civil = estado_civil

            email = form_data.get('cliente_email')
            cliente.cliente_email = email

            telefone_fixo = form_data.get('cliente_phone_fixo')
            cliente.cliente_phone_fixo = telefone_fixo

            celular = form_data.get('cliente_cel_phone')
            cliente.cliente_cel_phone = celular

            cpf = form_data.get('cliente_cpf')
            cliente.cliente_cpf = cpf


            cliente.save()

            return redirect('accounts:login')
    else:
        form_cadastro = Cadastro()

    context = {
        'title': 'cadastro',
        'form_cadastro': form_cadastro,
    }

    return render(request, tamplate_name, context)







