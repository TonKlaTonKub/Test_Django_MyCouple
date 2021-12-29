from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactMessage

# Create your views here.
def Home(request):
    return render(request, 'home/home.html')

def Service(request):
    return render(request, 'home/service.html')

def Contact(request):
    if request.method == 'POST':
        data = request.POST.copy()
        title = data.get('title')
        email = data.get('email')
        detail = data.get('detail')
        print(title, email, detail)
        
        new = ContactMessage()
        new.title = title
        new.email = email
        new.detail = detail
        new.save()

    return render(request, 'home/contact.html')