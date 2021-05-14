from django.shortcuts import render


def search_listings(request):
    if request.method == "POST":
        searched = request.POST['searched']

        return render(request, 'propertylistings.html', {'searched':searched})
    else:
        return render(request, 'propertylistings.html', {})
