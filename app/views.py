from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Post
class PostView(ListView):
    model = Post
    template_name = 'home.html'
class DetalView(DetailView):
    model = Post
    template_name = 'detal.html'
class CretView(CreateView):
    model = Post
    template_name = 'cret.html'
    fields = ['title','author','body']
class UpdatView(UpdateView):
    model = Post
    template_name = 'updat.html'
    fields = ['title','author','body']
class DeletView(DeleteView):
    model = Post
    template_name = 'delet.html'
    success_url=reverse_lazy('home')