import json
from django.shortcuts import render
from .models import Propertydetails


def search_listings(request):
    if request.method == "POST":

        searched = request.POST['searched']

        listings = Propertydetails.objects.filter(city__contains=searched)

        return render(request, 'propertylistings.html',
                      {'searched': searched,
                       'listings': listings})
    else:

        return render(request, 'propertylistings.html', {})

