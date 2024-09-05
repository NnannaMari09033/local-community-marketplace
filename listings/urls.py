from django.urls import path
from . import views

urlpatterns = [
    path('listings/', views.listing_list_create, name='listing-list-create'),
    path('listings/<int:pk>/', views.listing_detail, name='listing-detail'),
    path('listings/search/', views.search_listings, name='search-listings'),
    path('listings/filter/', views.filter_listings, name='filter-listings'),
]
