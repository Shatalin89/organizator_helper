from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from . import models
from . import forms
# Create your views here.

def get_halls(request):
    halls = models.Hall.objects.all()
    return render(request, 'halls.html', {'halls': halls})

def add_hall(request):
    if request.method == 'POST':
        form = forms.HallForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/halls/')
    else:
        form = forms.HallForm()
    return render(request, 'hall.html', {'form': form})

def edit_hall(request, hall_id):
    hall = get_object_or_404(models.Hall, id=hall_id)
    if request.method == "POST":
        form = forms.HallForm(request.POST, instance=hall)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/halls/')
    else:
        form = forms.HallForm(instance=hall)
    return render(request, 'edit_hall.html', {'form': form, 'hall': hall})

def del_hall(request, hall_id):
    hall = models.Hall.objects.get(id=hall_id)
    hall.delete()
    return HttpResponseRedirect('/halls/')


def get_shows(request):
    pass