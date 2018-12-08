from django.shortcuts import render, get_object_or_404
from .forms import Pais, Uf, Cidade, Bairro, Rua
from django.contrib.auth.decorators import login_required
from .models import Pais, Uf, Cidade, Bairro, Rua
# Create your views here.

# @login_required
# def dashboard(request):
#     return render(request, 'contas/dashboard.html')


def cadastro(request):
    tamplate_name = "cadastro.html"
    if request.method == 'POST':
        form_pais = Pais(request.POST or None);
        form_uf = Uf(request.POST or None);
        form_cidade = Cidade(request.POST or None);
        form_bairro = Bairro(request.POST or None);
        form_rua = Rua(request.POST or None);

        if form_pais.is_valid():
            form_data = form_pais.cleaned_data
            name = form_data.get('Nome do país')
            pais = Pais()
            pais.name = name
            pais.save()

        if form_uf.is_valid():
            form_data = form_uf.cleaned_data
            name = form_data.get('Nome do estado')
            bairro = Bairro()
            bairro.name = name
            bairro.save()

        if form_cidade.is_valid():
            form_data = form_cidade.cleaned_data
            name = form_data.get('Nome da cidade')
            cidade = Cidade()
            cidade.name = name
            cidade.save()

        if form_bairro.is_valid():
            form_data = form_bairro.cleaned_data
            name = form_data.get('Nome do bairro')
            bairro = Bairro()
            bairro.name = name
            bairro.save()

        if form_rua.is_valid():
            form_data = form_rua.cleaned_data
            name = form_data.get('Nome da rua')
            rua = Rua()
            rua.name = name
            rua.save()
    else:
        form_pais = Pais();
        form_uf = Uf();
        form_cidade = Cidade();
        form_bairro = Bairro();
        form_rua = Rua();


    context = {
        'title': 'cadastro',
        'form_pais': form_pais,
        'form_uf':form_uf,
        'form_cidade':form_cidade,
        'form_bairro':form_bairro,
        'form_rua':form_rua,
    }
    return render(request, tamplate_name, context)

def login(request):
    context = {
        'title': 'login',
    }
    return render(request, "login.html", context)



