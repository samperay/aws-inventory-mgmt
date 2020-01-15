from django.shortcuts import render
from django.http import HttpResponse
import django.db
import csv

reader  = csv.DictReader(open('inventory.csv', 'r'))
inventories = []
for line in reader:
    inventories.append(line)

info = inventories


def home(request):
    return render(request, 'inventory/home.html')

def getdata(request):

    context = {
        'info': info
        }
    return render(request, 'inventory/getdata.html', context)

def search(request):
    query = request.GET.get('q')
    matching = [ element for element in info if element['availability_zone'] == query ]

    context = {
        'match': matching
    }

    return render(request, 'inventory/search.html', context)
