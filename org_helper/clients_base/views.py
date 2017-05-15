from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.
from . import models
from . import forms
from django.shortcuts import redirect


def get_clients(request):
    clients = models.Clients.objects.all()
    return render(request, 'clients.html', {'clients' : clients})


def add_client(request):
    if request.method == 'POST':
        form = forms.ClientForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('/clients/')
    else:
        form = forms.ClientForm()
        return render(request, 'client.html', {'form' : form} )