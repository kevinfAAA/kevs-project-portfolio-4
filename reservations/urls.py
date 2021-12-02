from . import views
from django.urls import path


urlpatterns = [
    path('', views.ReservationsList.as_view(), name='reservations')
]