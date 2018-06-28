from django.conf.urls import url

from .views import (
#restaurant_listview,
RestaurantsListView,
RestaurantDetailView,
RestaurantCreateView,
#restaurant_createview,
)


urlpatterns = [
    url(r'^create/$', RestaurantCreateView.as_view(), name='create'),
    url(r'$', RestaurantsListView.as_view(),name='list'),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name='details'),
]
