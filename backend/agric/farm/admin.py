from django.contrib import admin
from .models import Officer, Farmer, Report, Season, Location


# Register your models here.
admin.site.register(Officer)
admin.site.register(Farmer)
admin.site.register(Report)
admin.site.register(Season)
admin.site.register(Location)
