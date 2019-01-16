
from django.urls import include, path
from . import views
from django.contrib.auth import views as logout
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth import urls


app_name = 'accounts'

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('', include('django.contrib.auth.urls')),


    ]




