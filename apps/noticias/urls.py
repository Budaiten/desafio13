from django.urls import path
from .views import NoticiaListView, NoticiaDetailView
from . import views

app_name = 'apps.noticias'

urlpatterns = [
    path('noticias/', NoticiaListView.as_view(), name='noticias'),
    path('noticias/<int:id>', NoticiaDetailView.as_view(), name='noticia_individual'),
]