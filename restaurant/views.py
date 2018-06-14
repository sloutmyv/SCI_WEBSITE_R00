from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .models import Restaurant
from .forms import RestaurantCreateForm

# def restaurant_createview(request):
#     form = RestaurantCreateForm(request.POST or None)
#     errors = None
#     if form.is_valid():
#         form.save()
#         # print('valid data')
#         # obj = Restaurant.objects.create(
#         #     name = form.cleaned_data.get('name'),
#         #     location = form.cleaned_data.get('location'),
#         #     category = form.cleaned_data.get('category'),
#         # )
#         return HttpResponseRedirect('/restaurant/')
#     if form.errors:
#         errors = form.errors
    # 
    # template_name = 'restaurant/forms.html'
    # context = {"form":form, "errors":errors}
    # return render(request,template_name,context)

class RestaurantCreateView(CreateView):
    form_class = RestaurantCreateForm
    template_name = 'restaurant/forms.html'
    success_url = '/restaurant/'


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

    # def get_object(self, *args, **kwargs):
    #     rest_id = self.kwargs.get('rest_id')
    #     obj = get_object_or_404(Restaurant, id=rest_id)
    #     return(obj)
