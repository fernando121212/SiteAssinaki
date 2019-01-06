
from django.urls import include, path
from . import views
from django.contrib.auth import views as login
from django.contrib.auth import views as logout


app_name = 'accounts'

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.form_login, name='login'),
    path('enviar_email_cadastro/', views.email_cadastro, name='enviar_email_cadastro'),
    # path('enviar_email_senha/', views.email_senha, name='enviar_email_senha'),

    # path('cadastro/', login.LoginView.as_view(template_name = 'cadastro.html'), name='cadastro'),
    # path('login/', login.LoginView.as_view(template_name='login.html'), name='login'),
    path('sair/', logout.LogoutView.as_view(next_page = 'core:index-light'), name='logout'),

]
