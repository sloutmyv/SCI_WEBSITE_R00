from django.conf.urls import url

from .views import (
RestaurantsListView,
RestaurantDetailView,
RestaurantCreateView,
RestaurantUpdateView,
)


urlpatterns = [
    url(r'^create/$', RestaurantCreateView.as_view(), name='create'),
    #url(r'^(?P<slug>[\w-]+)/edit/$', RestaurantUpdateView.as_view(), name='edit'),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantUpdateView.as_view(), name='details'),
    url(r'$', RestaurantsListView.as_view(),name='list'),
]
