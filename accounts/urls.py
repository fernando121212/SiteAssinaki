
from django.urls import include, path
from . import views
from django.contrib.auth import views as login
# from django.contrib.auth import views as logout

app_name = 'accounts'

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', login.LoginView.as_view(template_name = 'login.html'), name='login'),
    # path('logout/', login.LogoutView.as_view(template_name = 'login.html'), name='logout'),
]
