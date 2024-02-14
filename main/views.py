from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def s2(request):
    return render(request, 's2.html')

def dsa(request):
    return render(request, 'dsa.html')

def playlist(request):
    return render(request, 'playlist.html')

def notes(request):
    return render(request, 'notes.html')

def platforms(request):
    return render(request, 'platforms.html')

def coming(request):
    return render(request, 'coming.html')

def webdev(request):
    return render(request, 'webdev.html')

def fplaylist(request):
    return render(request, 'fplaylist.html')