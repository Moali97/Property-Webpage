from django.shortcuts import render


def home(request):
    return render(request, 'search.html')


def about(request):
    return render(request, 'about.html')
