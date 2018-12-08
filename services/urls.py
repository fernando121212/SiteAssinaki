
from django.urls import include, path
from . import views

app_name = 'services'

urlpatterns = [
    path('servicos/', views.services, name='services'),
]
