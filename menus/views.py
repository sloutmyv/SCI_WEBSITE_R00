from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import ItemForm
from .models import Item

class ItemListView(ListView):
    def get_queryset(self):
        queryset = Item.objects.filter(user=self.request.user)
        return queryset

class ItemDetailView(DetailView):
    def get_queryset(self):
        queryset = Item.objects.filter(user=self.request.user)
        return queryset

class ItemCreateView(CreateView):
    template_name = 'forms.html'
    form_class = ItemForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(ItemCreateView, self).form_valid(form)

    def get_queryset(self):
        queryset = Item.objects.filter(user=self.request.user)
        return queryset

    def get_context_data(self,*args,**kwargs):
        context = super(ItemCreateView, self).get_context_data(*args,**kwargs)
        context['title'] = 'Create Item'
        return context

class ItemUpdateView(UpdateView):
    template_name = 'forms.html'
    form_class = ItemForm
    def get_queryset(self):
        queryset = Item.objects.filter(user=self.request.user)
        return queryset

    def get_context_data(self,*args,**kwargs):
        context = super(ItemUpdateView, self).get_context_data(*args,**kwargs)
        context['title'] = 'Update Item'
        return context