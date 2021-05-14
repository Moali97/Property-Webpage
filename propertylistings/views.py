from django.shortcuts import render


def search_listings(request):
    return render(request, 'propertylistings.html', {})
