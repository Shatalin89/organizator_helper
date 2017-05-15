from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.
from . import models


def get_clients(request):
    clients = models.Clients.objects.all()
    return render(request, 'clients.html', {'clients' : clients})