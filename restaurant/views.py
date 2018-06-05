from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from django.views import View
from django.views.generic import TemplateView, ListView

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
