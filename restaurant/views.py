from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .models import Restaurant

def restaurant_listview(request):
    template_name = 'restaurant/restaurant_list.html'
    queryset = Restaurant.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request,template_name,context)

class RestaurantsListView(ListView):
    template_name = 'restaurant/restaurant_list.html'
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            queryset = Restaurant.objects.filter(Q(category__iexact=slug))
        else:
            queryset = Restaurant.objects.all()
        return queryset

class RestaurantDetailView(DetailView):
    queryset = Restaurant.objects.all()

    def get_context_data(self, *args, **kwargs):
        print(self.kwargs)
        context = super(RestaurantDetailView,self).get_context_data(*args,**kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        rest_id = self.kwargs.get('rest_id')
        obj = get_object_or_404(Restaurant, id=rest_id)
        return(obj)
