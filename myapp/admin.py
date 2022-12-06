from django.contrib import admin

from .models import Cow
from .models import FarmLocations
from .models import Product


admin.site.register(Cow)

admin.site.register(FarmLocations)
admin.site.register(Product)


