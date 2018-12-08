from django.shortcuts import render, get_object_or_404

# Create your views here.

def cadastro(request):
    contex = {'title': 'cadastro'}
    return render(request, "cadastro.html", contex)

def login(request):
    contex = {'title': 'login'}
    return render(request, "login.html", contex)


