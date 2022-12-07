from django.shortcuts import render, redirect
from .models import FarmLocations
from .models import Cow
from .models import Product



from django.http import HttpResponseRedirect
from .forms import CowForm
from .forms import LocationForm

from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required




import stripe


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY



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

@login_required(login_url='/members/login_user')
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
    return render(request, "cows.html",{'cow':cow}) 

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


    return render(request, 'farms.html', {'title':"Searched Farms...",'searched':searched, 'location_search':location_search})
  else:
    return render(request, "farms.html", context)
  
def all_farms(request):
  farm_list = FarmLocations.objects.all()
  cow_list = Cow.objects.all()
  total_cows = len(Cow.objects.all()) -1
  context={

    "title":"All Farms",
    "farm_list":farm_list,
    "cow_list":cow_list,
    "total_cows":total_cows
  }

  return render(request, "all_farms.html", context)


def single_cow(request, cow_id):
  cow = Cow.objects.get(pk=cow_id)
  childrenlist = cow.children.all()
  childrenlength = len(cow.children.all())
  context={
    'title':"Cow",
    'cow':cow,
    'childrenlength':childrenlength,
    'childrenlist':childrenlist
  }
  return render(request, "single_cow.html",context) 


def single_farm(request, farm_id):
  farm = FarmLocations.objects.get(pk=farm_id)
  cowlist = Cow.objects.filter(cow_location__location_name__contains=farm.location_name)
  context={
    'title':"Farm",
    'farm':farm, 
    'cowlist':cowlist
  }
  return render(request, "single_farm.html",context) 



def update_cow(request, cow_id):
  cow = Cow.objects.get(pk=cow_id)
  form = CowForm(request.POST or None, instance=cow )
  if form.is_valid():
    form.save()
    return redirect('/cows/all-cows')
  return render(request, 'update_cow.html',{'cow':cow, 'form':form, 'title':"Update Cow..."})

def update_farm(request, farm_id):
  farm = FarmLocations.objects.get(pk=farm_id)
  form = LocationForm(request.POST or None, instance=farm )
  if form.is_valid():
    form.save()
    return redirect('/farms/all-farms')
  return render(request, 'update_farm.html',{'farm':farm, 'form':form, 'title':"Update Farm..."})


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        price = Price.objects.get(id=self.kwargs["pk"])
        domain = "https://yourdomain.com"
        if settings.DEBUG:
            domain = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=domain + '/success/',
            cancel_url=domain + '/cancel/',
        )
        return redirect(checkout_session.url)





class SuccessView(TemplateView):
    template_name = "success.html"

class CancelView(TemplateView):
    template_name = "cancel.html"

class ProductLandingPageView(TemplateView):
    template_name = "meat.html"

    def get_context_data(self, **kwargs):
        product = Product.objects.get(name="5lbs meat")
        price = Product.price
        context = super(ProductLandingPageView,
                        self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "prices": price
        })
        return context