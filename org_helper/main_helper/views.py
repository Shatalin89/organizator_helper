from django.shortcuts import render, render_to_response


# Create your views here.

def index(request):
    return render_to_response('admin.html')

def main_org(request):
    return render_to_response('main.html')