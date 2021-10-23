import json
from django.shortcuts import render
from .models import Propertydetails


def search_listings(request):
    if request.method == "POST":

        searched = request.POST['searched']
        # filters through city name given
        listings = Propertydetails.objects.filter(city__contains=searched)
        context = {'searched': searched,
                   'listings': listings,
                   }

        return render(request, 'propertylistings.html', context)

    else:

        return render(request, 'propertylistings.html', {})

#web: gunicorn propertyweb.wsgi --log-file -