from django.shortcuts import render, get_object_or_404


# Create your views here.

def cadastro(request):
    return render(request, "cadastro.html")

def login(request):
    return render(request, "login.html")