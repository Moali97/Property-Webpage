from django.urls import path
from . import views

urlpatterns = [
    path('propertylistings', views.search_listings, name='propertylistings'),
]