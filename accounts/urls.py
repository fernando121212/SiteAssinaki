
from django.urls import include, path
from . import views
from django.contrib.auth import views as login
from django.contrib.auth import views as logout


app_name = 'accounts'

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    # path('login/', views.details, name='login

    path('login/', login.LoginView.as_view(template_name = 'login.html'), name='login'),
    path('sair/', logout.LogoutView.as_view(next_page = 'core:index-light'), name='logout'),

]
