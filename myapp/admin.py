from django.contrib import admin

from .models import Cow
from .models import FarmLocations

admin.site.register(Cow)

admin.site.register(FarmLocations)