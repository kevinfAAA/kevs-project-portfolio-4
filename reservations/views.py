from django.shortcuts import render
from django.views import generic
from .models import Reservations


class ReservationsList(generic.ListView):
    model = Reservations
    template_name = 'reservations.html'

# Create your views here.
