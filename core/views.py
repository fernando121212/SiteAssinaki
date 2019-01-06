
from django.shortcuts import render, get_object_or_404
from .models import Tipo_documento, Release,  PrecoAssinatura, StatusPagamento


def index_light(request):

    tamplate_name = "index-light.html"

    context = {
            'title': 'home',
            'tiposs_documentos': Tipo_documento.objects.all(),
            'releases': Release.objects.all(),
            'PrecoAssinatura': PrecoAssinatura.objects.all(),
            'StatusPagamentos': StatusPagamento.objects.all(),
        }
    return render(request, tamplate_name, context)

def about(request):
    context = {
        'title': 'Sobre a empresa'
    }
    return render(request, "about.html", context)

def clients(request):
    context = {
        'title': 'clientes'
    }
    return render(request, "clients.html", context)

def contact(request):
    context = {
        'title': 'fale!'
    }
    return render(request, "contact.html", context)

