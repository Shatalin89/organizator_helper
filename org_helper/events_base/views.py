from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateResponseMixin, View

from . import models
from . import forms
from django.urls import reverse
# Create your views here.


def get_halls(request):
    halls = models.Hall.objects.all()
    return render(request, 'halls/halls.html', {'halls': halls})


def add_hall(request):
    if request.method == 'POST':
        form = forms.HallForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('halls'))
    else:
        form = forms.HallForm()
    return render(request, 'halls/hall.html', {'form': form})


def edit_hall(request, hall_id):
    hall = get_object_or_404(models.Hall, id=hall_id)
    if request.method == "POST":
        form = forms.HallForm(request.POST, instance=hall)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('halls'))
    else:
        form = forms.HallForm(instance=hall)
    return render(request, 'halls/edit_hall.html', {'form': form, 'hall': hall})


def del_hall(request, hall_id):
    hall = models.Hall.objects.get(id=hall_id)
    hall.delete()
    return HttpResponseRedirect(reverse('halls'))


def get_shows(request):
    shows = models.Shows.objects.all()
    return render(request, 'shows/shows.html', {'shows': shows})


def add_show(request):
    if request.method == 'POST':
        form = forms.ShowForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('shows'))
    else:
        form = forms.ShowForm()
    return render(request, 'shows/show.html', {'form': form})


def edit_show(request, show_id):
    shows = get_object_or_404(models.Shows, id=show_id)
    if request.method == "POST":
        form = forms.ShowForm(request.POST, instance=shows)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('shows'))
    else:
        form = forms.ShowForm(instance=shows)
    return render(request, 'shows/edit_show.html', {'form': form, 'shows': shows})

def del_show(request, show_id):
    show = models.Shows.objects.get(id=show_id)
    show.delete()
    return HttpResponseRedirect(reverse('shows'))


def get_info(request):
    infos = models.EventsInfo.objects.all()
    return render(request, 'eventsinfo/eventsinfo.html', {'infos': infos})

def add_info(request):
    if request.method == 'POST':
        form = forms.EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('events'))
    else:
        form = forms.EventForm()
    return render(request, 'eventsinfo/eventinfo.html', {'form': form})

def edit_info(request, info_id):
    event = get_object_or_404(models.EventsInfo, id=info_id)
    if request.method == "POST":
        form = forms.EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('events'))
    else:
        form = forms.EventForm(instance=event)
    return render(request, 'eventsinfo/edit_eventinfo.html', {'form': form, 'infos': event})

def del_info(request, info_id):
    event = models.EventsInfo.objects.get(id=info_id)
    event.delete()
    return HttpResponseRedirect(reverse('events'))

def reg_client(request):
    infos = models.EventsInfo.objects.filter(event_state=True)
    clients = models.Clients.objects.all()
    client_list = []
    j = 0
    z = 0
    tmp = {}
    for i in clients:
        tmp[j] = i
        j += 1
        if j == 3:
            j = 0
            client_list.append(tmp)
            tmp = {}
    if j != 0:
        client_list.append(tmp)
    return render(request, 'eventreg/regclient.html', {'infos': infos, 'client_list': client_list})

def add_reg(request):
    if request.method == 'POST':
        form = forms.EventRegForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('events'))
    else:
        form = forms.EventRegForm()
    return render(request, 'eventreg/regclient_2.html', {'forms': form})


class RegCLient(TemplateResponseMixin, View):
    template_name = 'eventreg/regclient_2.html'

    def dispatch(self, request, *args, **kwargs):
        FS = modelformset_factory(forms.EventRegForm, extra=1)
        queryset = models.EventPlace.objects.all()

        if request.method == 'POST':
            formset = FS(request.POST, request.FILES)

            if formset.is_valid():
                formset.save()
                formset = FS(queryset=queryset)

        else:
            formset = FS(queryset=queryset)
        return self.render_to_response({'forms': forms})