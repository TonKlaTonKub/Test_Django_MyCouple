from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return render(request, 'home/home.html')

def Service(request):
    return render(request, 'home/service.html')

def Contact(request):
    return render(request, 'home/contact.html')