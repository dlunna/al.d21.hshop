from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def webmaster(request):
    return render(request, 'core/webmaster.html')


