from django.http import HttpResponseRedirect
from django.shortcuts import render
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