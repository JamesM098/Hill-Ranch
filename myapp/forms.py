from django import forms
from django.forms import ModelForm
from .models import Cow
from .models import FarmLocations


class CowForm(ModelForm):
 class Meta:
  model = Cow
  fields = ('cow_tag', 'cow_sex', 'cow_vaccinations', 'cow_location', 'cow_notes', 'cow_PARENT')


class LocationForm(ModelForm):
 class Meta:
  model = FarmLocations
  fields = ('location_name','location_description')