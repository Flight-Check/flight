from django.contrib import admin

# Register your models here.
from flight_detail.models import Flightinfo


class CustomFlightInfo(admin.ModelAdmin):
    list_display = ('id', 'airline', 'flightnumbers')
    search_fields = ('id', 'flightnumbers')


admin.site.register(Flightinfo, CustomFlightInfo)
