from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import TodoModel
from django.urls import reverse_lazy
# Create your views here.


class Todolist(ListView):
    template_name = 'templates/list.html'
    model = TodoModel

class Tododetail(DetailView):
    template_name = 'templates/detail.html'
    model = TodoModel

class Todocreate(CreateView):
    template_name = 'templates/create.html'
    model = TodoModel
    fields = ('title','memo','priority','duedate')
    success_url = reverse_lazy('list')

class Tododelete(DeleteView):
    template_name ='templates/delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')

class Todoupdate(UpdateView):
    template_name ='templates/update.html'
    model = TodoModel
    fields = ('title','memo','priority','duedate')
    success_url =reverse_lazy('list')