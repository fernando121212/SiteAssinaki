from django.shortcuts import render
from .forms import Cliente

def cliente(request):
    template_name = 'formulario'
    return render(request,template_name)

# Create your views here.
