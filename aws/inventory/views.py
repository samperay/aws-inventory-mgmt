from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Invs

def home(request):
    return render(request, 'inventory/home.html')

def getdata(request):
    info = Invs.objects.all()
    context = {
        'info': info
        }
    return render(request, 'inventory/getdata.html', context)

def search(request,availability_zone):
    try:
        info = Invs.objects.get(availability_zone=availability_zone)
    except Invs.DoesNotExist:
        raise Http404('availability_zone not found')
    return render(request, 'inventory/search.html', {'info': info})
