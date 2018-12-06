
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

class IndexView(generic.ListView):
    template_name = "index-light.html"

    def get_queryset(self):
        pass

# def index_light(request):
#     return render(request, "index-light.html")

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def clients(request):
    return render(request, "clients.html")

def contact(request):
    return render(request, "contact.html")

def login(request):
    return render(request, "login.html")

def cadastro(request):
    return render(request, "cadastro.html")

def formulario(request):
    return render(request, "formulario.html")

