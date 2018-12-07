from django.shortcuts import render
from .forms import Cliente

def cliente(request):
    template_name = 'formulario'
    if request.method == "POST":
        form = Cliente(request.POST)
    else:
        form=cliente()
    context = {
        'form': form
    }
    return render(request,template_name, context)



# Create your views here.
