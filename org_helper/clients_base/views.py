from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
# Create your views here.
from . import models
from . import forms

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def get_clients(request):
    clients = models.Clients.objects.all()
    paginator = Paginator(clients, 20)
    page = request.GET.get('page')
    try:
        client = paginator.page(page)
    except PageNotAnInteger:
        client = paginator.page(1)
    except EmptyPage:
        client = paginator.page(paginator.num_pages)
    return render(request, 'clients.html', {'clients' : client})


def add_client(request):
    if request.method == 'POST':
        form = forms.ClientForm(request.POST)
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


def del_client(request, clients_id):
    client = models.Clients.objects.get(id=clients_id)
    client.delete()
    return HttpResponseRedirect('/clients/')