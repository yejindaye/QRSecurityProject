from django.contrib import admin
from .models import *

admin.site.register(Resident)
admin.site.register(Visitor)
admin.site.register(Apartment)
# admin.site.register(Building)
# admin.site.register(Floor)
# admin.site.register(Room)