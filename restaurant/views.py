from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from .models import Restaurant
from .forms import RestaurantCreateForm


class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantCreateForm
    login_url='/login/'
    template_name = 'forms.html'
    #success_url = '/restaurant/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(RestaurantCreateView, self).form_valid(form)

    def get_context_data(self,*args,**kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args,**kwargs)
        context['title'] = 'Add Restaurant'
        return context


class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    form_class = RestaurantCreateForm
    login_url='/login/'
    template_name = 'restaurant/detail-update.html'

    def get_context_data(self,*args,**kwargs):
        context = super(RestaurantUpdateView, self).get_context_data(*args,**kwargs)
        context['title'] = 'Add Restaurant'
        return context

    def get_queryset(self):
        return Restaurant.objects.filter(user=self.request.user)

# class RestaurantsListView(ListView):
#     template_name = 'restaurant/restaurant_list.html'
#
#     def get_queryset(self):
#         slug = self.kwargs.get('slug')
#         if slug:
#             queryset = Restaurant.objects.filter(Q(category__iexact=slug))
#         else:
#             queryset = Restaurant.objects.all()
#         return queryset

class RestaurantsListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Restaurant.objects.filter(user=self.request.user)

class RestaurantDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        return Restaurant.objects.filter(user=self.request.user)

    # def get_object(self, *args, **kwargs):
    #     rest_id = self.kwargs.get('rest_id')
    #     obj = get_object_or_404(Restaurant, id=rest_id)
    #     return(obj)
