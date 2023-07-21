from django.shortcuts import render
from .models import Noticia
from django.views.generic import ListView, DetailView

class NoticiaListView(ListView):
    model = Noticia
    template_name = 'noticia.html'
    context_object_name = 'noticias'

class NoticiaDetailView(DetailView):
    model = Noticia
    template_name = 'noticias/noticia_individual.html'
    context_object_name = 'noticias'
    pk_url_kwarg = 'id'
    queryset = Noticia.objects.all()