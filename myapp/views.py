from django.shortcuts import render
from .models import FarmLocations
from .models import Cow

from django.http import HttpResponseRedirect
from .forms import CowForm
from .forms import LocationForm
# Create your views here.

def add_location(request):
  submitted = False
  form = LocationForm
  if request.method == "POST":
    form = LocationForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/farms/all-farms')
    else:
      form = LocationForm
      if 'submitted' in request.GET:
        submitted = True
  return render(request, "add_location.html",{'title':'Add a Location...','form':form, 'submitted':submitted}) 


def add_cow(request):
  submitted = False
  form = CowForm
  if request.method == "POST":
    form = CowForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/cows/all-cows')
    else:
      form = CowForm
      if 'submitted' in request.GET:
        submitted = True
  return render(request, "add_cow.html",{'title':'Add a Cow...','form':form, 'submitted':submitted}) 







def show_cows(request, cow_id):
    cow = Cow.objects.get(pk=cow_id)
    return render(request, "show_cow.html",{'cow':cow}) 

def show_farms(request, farm_id):
    farm = FarmLocations.objects.get(pk=farm_id)
    return render(request, "show_farm.html",{'farm':farm}) 



def index(request, page=0):
  context ={
    "title":"Home",
  }
  return render(request, "index.html", context=context) 


def cows(request):
  context = {"title":"Cows"}
  if request.method == "POST":
    searched = request.POST['searched']
    name_search = Cow.objects.filter(cow_tag__contains=searched)
    location_search = Cow.objects.filter(cow_location__location_name__contains=searched)
    return render(request, 'cows.html', {'title':"Cows",'searched':searched, 'name_search':name_search, 'location_search':location_search})
  else:
    return render(request, "cows.html", context)


def all_cows(request):
  cow_list = Cow.objects.all()
  context={

    "title":"All Cows",
    "cow_list":cow_list
  }
  return render(request, "all_cows.html", context)



def farms(request):
  context = {"title":"Farms"}
  if request.method == "POST":
    searched = request.POST['locSearch']
    location_search = FarmLocations.objects.filter(location_name__contains=searched)


    return render(request, 'farms.html', {'title':"Cows",'locSearch':searched, 'location_search':location_search})
  else:
    return render(request, "farms.html", context)
  
def all_farms(request):
  farm_list = FarmLocations.objects.all()
  context={

    "title":"All Farms",
    "farm_list":farm_list
  }

  return render(request, "all_farms.html", context)