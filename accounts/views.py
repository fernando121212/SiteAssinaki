from .forms import Cadastro, LoginForm, Email
from django.template.defaultfilters import slugify
from .models import Cliente, Pais, Uf, Cidade, Bairro, Rua, Pessoa_juridica, Dados_cartao
from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse


def email_cadastro(request):
    tamplate_name = 'login.html'
    context = {}
    if request.method == 'POST':
        form = Email(request.POST)
        if form.is_valid():

             context['is_valid'] = True
             form = Email()
             form.enviar_email()

        return redirect('accounts:login')

    else:
        form = Email()
        context['form'] = form
    return render(request, tamplate_name, context)


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

                    return redirect('core:index-light')
                else:
                    return HttpResponse('Desabilitar account')
            else:
                return HttpResponse('Login Inválido')
    else:
        form = LoginForm()
    context = {
            'title': 'login',
            'form': form,
    }

    return render(request, 'login.html', context)

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
            pais, pais_novo = Pais.objects.get_or_create(
                name = name_pais,
                slug = slugify(name_pais)
            )
            if pais_novo == True:
                pais.save()

            name_uf = form_data.get('name_uf')
            uf, uf_novo = Uf.objects.get_or_create(
                name = name_uf,
                slug = slugify(name_uf),
                pais = pais
            )
            if uf_novo == True:
                uf.save()

            name_cidade = form_data.get('name_cidade')
            cidade, cidade_nova = Cidade.objects.get_or_create(
                name = name_cidade,
                slug = slugify(name_cidade),
                uf = uf
            )
            if cidade_nova == True:
                cidade.save()

            name_bairro = form_data.get('name_bairro')
            bairro, bairro_novo = Bairro.objects.get_or_create(
                name = name_bairro,
                slug = slugify(name_bairro),
                cidade = cidade
            )
            if bairro_novo == True:
                bairro.save()

            name_rua = form_data.get('name_rua')
            rua_numero = form_data.get('rua_numero')
            rua_complemento = form_data.get('rua_complemento')
            rua_cep = form_data.get('rua_cep')
            rua, rua_nova = Rua.objects.get_or_create(
                name = name_rua,
                slug = slugify(name_rua),
                rua_numero = rua_numero,
                rua_complemento = rua_complemento,
                rua_cep = rua_cep,
                bairro = bairro
            )
            if rua_nova == True:
                rua.save()

            first_name = form_data.get('first_name' )
            last_name = form_data.get('last_name')
            cliente_data_nascimento = form_data.get('cliente_data_nascimento')
            cliente_estado_civil = form_data.get('cliente_estado_civil')
            email = form_data.get('email')
            cliente_phone_fixo = form_data.get('cliente_phone_fixo')
            cliente_cel_phone = form_data.get('cliente_cel_phone')
            cliente_cpf = form_data.get('cliente_cpf')
            cliente, cliente_novo = Cliente.objects.get_or_create(
                first_name = first_name,
                slug = slugify(first_name, last_name),
                last_name = last_name,
                cliente_data_nascimento = cliente_data_nascimento,
                cliente_estado_civil = cliente_estado_civil,
                email=email,
                cliente_phone_fixo = cliente_phone_fixo,
                cliente_cel_phone = cliente_cel_phone,
                cliente_cpf = cliente_cpf,
                rua=rua
            )

            if cliente_novo == True:
                cliente.save()

            return redirect('accounts:login')
    else:
        form_cadastro = Cadastro()

    context = {
        'title': 'cadastro',
        'form_cadastro': form_cadastro,
    }

    return render(request, tamplate_name, context)







