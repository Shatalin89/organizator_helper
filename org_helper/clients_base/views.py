from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
# Create your views here.
from . import models
from . import forms
from django.shortcuts import redirect


def get_clients(request):
    clients = models.Clients.objects.all()
    return render(request, 'clients.html', {'clients' : clients})


def add_client(request):
    print(request.method == 'POST')
    if request.method == 'POST':
        form = forms.ClientForm(request.POST)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/clients/')
    else:
        form = forms.ClientForm()
    return render(request, 'client.html', {'form': form})

def edit_client(request, clients_id=None):
    client = get_object_or_404(models.Clients, id=clients_id)
    if request.method == "POST":
        form = forms.ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/clients/')
    else:
        form = forms.ClientForm(instance=client)
    return render(request, 'edit_client.html', {'form': form, 'client': client})