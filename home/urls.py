from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home-page'),
    path('service/', Service, name='service'),
    path('contact/', Contact, name='contact',)
]