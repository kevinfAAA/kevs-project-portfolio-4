from django.shortcuts import render
from django.views import generic


def index(request):
        return render(request, 'index.html', {})

def reservations(request):
        return render(request, 'reservations.html', {})

def login(request):
        return render(request, 'login.html', {})

def register(request):
        return render(request, 'register.html', {})

# Create your views here.
