
from django.shortcuts import render, get_object_or_404
from django.views  import generic


# Create your views here.
# def index(request):
#     context = {
#         'title': 'services',
#         'pagina_1': 'A empresa',
#         'pagina_2': 'Serviços',
#         'pagina_3': 'Cadastre-se',
#         'pagina_4': 'Login',
#     }
#     return render(request, "index.html", context)

# class IndexView(generic.ListView):
#     template_name = "index-light.html"
#
#     context = {
#         'title': 'home'
#     }
#
#     # def get_context_data(self, **kwargs):
#     #     context = super(IndexView, self).get_context_data(**kwargs)
#     #     return context
#
#
#
#     def get_queryset(self):
#       pass

def index_light(request):
    context = {
            'title': 'home'
        }
    return render(request, "index-light.html", context)

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

