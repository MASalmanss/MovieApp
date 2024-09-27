from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request , "index.html")

def movies(request):
    pass

def movie_details(request , slug ):
    return 
